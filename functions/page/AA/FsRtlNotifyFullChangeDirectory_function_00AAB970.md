# FsRtlNotifyFullChangeDirectory

- RVA: `0x00AAB970`–`0x00AAB9CC` (길이 `92` bytes)
- VA: `0x0000000140AAB970`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007A034`
- 디코드: `19`개 명령, `92/92` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AAB9C1` → [FsRtlNotifyFilterChangeDirectory](FsRtlNotifyFilterChangeDirectory_function_00AAB9E0.md) (function, `0x00AAB9E0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AAB970  4C 8B DC                        mov r11, rsp
00AAB973  48 83 EC 68                     sub rsp, 0x68
00AAB977  49 83 63 E8 00                  and qword ptr [r11 - 0x18], 0
00AAB97C  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
00AAB984  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
00AAB988  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
00AAB990  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
00AAB994  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
00AAB99C  49 89 43 D0                     mov qword ptr [r11 - 0x30], rax
00AAB9A0  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
00AAB9A7  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00AAB9AB  8A 84 24 98 00 00 00            mov al, byte ptr [rsp + 0x98]
00AAB9B2  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00AAB9B6  8A 84 24 90 00 00 00            mov al, byte ptr [rsp + 0x90]
00AAB9BD  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00AAB9C1  E8 1A 00 00 00                  call 0x140aab9e0
00AAB9C6  48 83 C4 68                     add rsp, 0x68
00AAB9CA  C3                              ret
00AAB9CB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlNotifyFullChangeDirectory(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int8 a5, unsigned __int8 a6, unsigned int a7, __int64 a8, __int64 a9, __int64 a10)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m38;
    unsigned __int8 v_stack_m40;
    unsigned __int8 v_stack_m48;

    v_rsp = (v_rsp) - (104);
    *(unsigned __int64 *)(v_rsp - 32) = a10;
    *(unsigned __int64 *)(v_rsp - 40) = a9;
    *(unsigned __int64 *)(v_rsp - 48) = a8;
    v_stack_m38 = (unsigned int)((unsigned int)(a7));
    v_stack_m40 = a6;
    v_stack_m48 = a5;
    result = FsRtlNotifyFilterChangeDirectory(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (104);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlNotifyFullChangeDirectory(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint8_t Arg5, uint8_t Arg6, uint32_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m38;
    uint8_t v_stack_m40;
    uint8_t v_stack_m48;

    local_rsp = (local_rsp) - (104);
    *(uint64_t *)(local_rsp - 0x20) = Arg10;
    *(uint64_t *)(local_rsp - 0x28) = Arg9;
    *(uint64_t *)(local_rsp - 0x30) = Arg8;
    v_stack_m38 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m40 = Arg6;
    v_stack_m48 = Arg5;
    result = FsRtlNotifyFilterChangeDirectory(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (104);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AAB970&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AAB970[BB_00AAB970]
  bb_00AAB9CB[BB_00AAB9CB]
```
