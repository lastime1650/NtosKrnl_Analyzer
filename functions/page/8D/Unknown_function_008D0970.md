# sub_008D0970

- RVA: `0x008D0970`–`0x008D09C6` (길이 `86` bytes)
- VA: `0x00000001408D0970`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00084AC0`
- 디코드: `26`개 명령, `86/86` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008D09A5` → [sub_008D3DC0](Unknown_function_008D3DC0.md) (function, `0x008D3DC0`)
- `0x008D09B5` → [sub_00702150](../70/Unknown_function_00702150.md) (function, `0x00702150`)

### Direct callers
- [sub_008D18D4](Unknown_function_008D18D4.md) at `0x008D1982`
- [sub_008D379C](Unknown_function_008D379C.md) at `0x008D3A11`
- [sub_0099FC70](../99/Unknown_function_0099FC70.md) at `0x0099FE08`
- [sub_009A09B8](../9A/Unknown_function_009A09B8.md) at `0x009A0BA3`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008D0970  4C 8B DC                        mov r11, rsp
008D0973  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
008D0977  57                              push rdi
008D0978  48 83 EC 30                     sub rsp, 0x30
008D097C  49 8B C1                        mov rax, r9
008D097F  48 8B FA                        mov rdi, rdx
008D0982  45 8B 4B 30                     mov r9d, dword ptr [r11 + 0x30]
008D0986  48 8B D9                        mov rbx, rcx
008D0989  41 83 F9 FF                     cmp r9d, -1
008D098D  75 20                           jne 0x1408d09af
008D098F  44 8B 44 24 60                  mov r8d, dword ptr [rsp + 0x60]
008D0994  49 8D 4B 30                     lea rcx, [r11 + 0x30]
008D0998  49 89 4B E8                     mov qword ptr [r11 - 0x18], rcx
008D099C  45 33 C9                        xor r9d, r9d
008D099F  48 8B CB                        mov rcx, rbx
008D09A2  48 8B D0                        mov rdx, rax
008D09A5  E8 16 34 00 00                  call 0x1408d3dc0
008D09AA  44 8B 4C 24 68                  mov r9d, dword ptr [rsp + 0x68]
008D09AF  48 8B D7                        mov rdx, rdi
008D09B2  48 8B CB                        mov rcx, rbx
008D09B5  E8 96 17 E3 FF                  call 0x140702150
008D09BA  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
008D09BF  48 83 C4 30                     add rsp, 0x30
008D09C3  5F                              pop rdi
008D09C4  C3                              ret
008D09C5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_008D0970(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    v_rsp = (v_rsp) - (48);
    result = a4;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp + 48)))) == -1) {
        a3 = a5;
        a1 = v_rsp + 48;
        *(unsigned __int64 *)(v_rsp - 24) = a1;
        a4 = 0;
        a1 = a1;
        a2 = 0;
        result = sub_008D3DC0(a1, a2, a3, a4);
        a4 = a6;
    }
    result = sub_00702150(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_008D0970(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    local_rsp = (local_rsp) - (48);
    result = Arg4;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp + 0x30)))) == -1) {
        Arg3 = Arg5;
        Arg1 = local_rsp + 48;
        *(uint64_t *)(local_rsp - 0x18) = Arg1;
        Arg4 = 0;
        Arg1 = Arg1;
        Arg2 = 0;
        result = sub_008D3DC0(Arg1, Arg2, Arg3, Arg4);
        Arg4 = Arg6;
    }
    result = sub_00702150(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008D0970&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008D0970[BB_008D0970]
  bb_008D098F[BB_008D098F]
  bb_008D09AF[BB_008D09AF]
  bb_008D09C5[BB_008D09C5]
  bb_008D0970 -->|branch| bb_008D09AF
  bb_008D0970 -->|fallthrough| bb_008D098F
  bb_008D098F -->|flow| bb_008D09AF
```
