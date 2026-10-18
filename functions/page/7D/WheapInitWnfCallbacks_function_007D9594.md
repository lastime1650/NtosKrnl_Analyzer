# WheapInitWnfCallbacks

- RVA: `0x007D9594`–`0x007D95ED` (길이 `89` bytes)
- VA: `0x00000001407D9594`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00097934`
- 디코드: `20`개 명령, `89/89` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x007D95D2` → [ExSubscribeWnfStateChange](../9D/ExSubscribeWnfStateChange_function_009D4BC0.md) (function, `0x009D4BC0`)

### Direct callers
- [WheaInitialize](../../init/C5/WheaInitialize_function_00C54C08.md) at `0x00C54E93`

### Static image references
- `0x007D95A0` → RVA `0x00661D70` (`WheapProcessOfflineList`; read)
- `0x007D95AC` → RVA `0x00020BC8` (`.rdata`; read)
- `0x007D95B3` → RVA `0x00EF7D08` (`.data`; read/write)
- `0x007D95BF` → RVA `0x00EF7D00` (`.data`; read/write)
- `0x007D95E0` → RVA `0x00EF7D18` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007D9594  4C 8B DC                        mov r11, rsp
007D9597  48 83 EC 38                     sub rsp, 0x38
007D959B  49 83 63 F0 00                  and qword ptr [r11 - 0x10], 0
007D95A0  48 8D 05 C9 87 E8 FF            lea rax, [rip - 0x177837]
007D95A7  49 83 63 08 00                  and qword ptr [r11 + 8], 0
007D95AC  48 8D 15 15 76 84 FF            lea rdx, [rip - 0x7b89eb]
007D95B3  48 83 25 4D E7 71 00 00         and qword ptr [rip + 0x71e74d], 0
007D95BB  49 8D 4B 08                     lea rcx, [r11 + 8]
007D95BF  48 83 25 39 E7 71 00 00         and qword ptr [rip + 0x71e739], 0
007D95C7  45 33 C9                        xor r9d, r9d
007D95CA  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
007D95CE  45 8D 41 01                     lea r8d, [r9 + 1]
007D95D2  E8 E9 B5 1F 00                  call 0x1409d4bc0
007D95D7  85 C0                           test eax, eax
007D95D9  78 0C                           js 0x1407d95e7
007D95DB  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
007D95E0  48 89 05 31 E7 71 00            mov qword ptr [rip + 0x71e731], rax
007D95E7  48 83 C4 38                     add rsp, 0x38
007D95EB  C3                              ret
007D95EC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WheapInitWnfCallbacks(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (56);
    a4 = 0;
    *(unsigned __int64 *)(v_rsp - 24) = v_rip - 1538103;
    result = ExSubscribeWnfStateChange(v_rsp + 8, v_rip - 8096235, a4 + 1, a4);
    if (!(sign_flag)) {
        result = v_stack_p8;
        *(unsigned __int64 *)(v_rip + 7464753) = result;
    }
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t WheapInitWnfCallbacks(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (56);
    Arg4 = 0;
    *(uint64_t *)(local_rsp - 0x18) = v_rip - 1538103;
    result = ExSubscribeWnfStateChange(local_rsp + 8, v_rip - 8096235, Arg4 + 1, Arg4);
    if (!(sign_flag)) {
        result = v_stack_p8;
        *(uint64_t *)(v_rip + 0x71E731) = result;
    }
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007D9594&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007D9594[BB_007D9594]
  bb_007D95DB[BB_007D95DB]
  bb_007D95E7[BB_007D95E7]
  bb_007D95EC[BB_007D95EC]
  bb_007D9594 -->|branch| bb_007D95E7
  bb_007D9594 -->|fallthrough| bb_007D95DB
  bb_007D95DB -->|flow| bb_007D95E7
```
