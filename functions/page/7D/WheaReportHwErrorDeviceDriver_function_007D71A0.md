# WheaReportHwErrorDeviceDriver

- RVA: `0x007D71A0`–`0x007D71E4` (길이 `68` bytes)
- VA: `0x00000001407D71A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CC98`
- 디코드: `16`개 명령, `68/68` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007D71D9` → [WheaReportHwErrorDeviceDriverEx](../../text/65/WheaReportHwErrorDeviceDriverEx_function_0065EA30.md) (function, `0x0065EA30`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007D71D9` → [WheaReportHwErrorDeviceDriverEx](../../text/65/WheaReportHwErrorDeviceDriverEx_function_0065EA30.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007D71A0  4C 8B DC                        mov r11, rsp
007D71A3  48 83 EC 58                     sub rsp, 0x58
007D71A7  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
007D71AF  45 33 D2                        xor r10d, r10d
007D71B2  49 89 43 F0                     mov qword ptr [r11 - 0x10], rax
007D71B6  8B 84 24 88 00 00 00            mov eax, dword ptr [rsp + 0x88]
007D71BD  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
007D71C1  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
007D71C9  45 89 53 E0                     mov dword ptr [r11 - 0x20], r10d
007D71CD  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
007D71D1  45 89 53 D0                     mov dword ptr [r11 - 0x30], r10d
007D71D5  4D 89 53 C8                     mov qword ptr [r11 - 0x38], r10
007D71D9  E8 52 78 E8 FF                  call 0x14065ea30
007D71DE  48 83 C4 58                     add rsp, 0x58
007D71E2  C3                              ret
007D71E3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WheaReportHwErrorDeviceDriver(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, __int64 a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;
    unsigned int v_stack_m18;

    v_rsp = (v_rsp) - (88);
    v_r10 = 0;
    *(unsigned __int64 *)(v_rsp - 16) = a7;
    v_stack_m18 = (unsigned int)((unsigned int)(a6));
    *(unsigned int *)(v_rsp - 32) = 0;
    *(unsigned __int64 *)(v_rsp - 40) = a5;
    *(unsigned int *)(v_rsp - 48) = 0;
    *(unsigned __int64 *)(v_rsp - 56) = 0;
    result = WheaReportHwErrorDeviceDriverEx(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t WheaReportHwErrorDeviceDriver(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, int64_t Arg7)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;
    uint32_t v_stack_m18;

    local_rsp = (local_rsp) - (88);
    local_r10 = 0;
    *(uint64_t *)(local_rsp - 0x10) = Arg7;
    v_stack_m18 = (uint32_t)((uint32_t)(Arg6));
    *(uint32_t *)(local_rsp - 0x20) = 0;
    *(uint64_t *)(local_rsp - 0x28) = Arg5;
    *(uint32_t *)(local_rsp - 0x30) = 0;
    *(uint64_t *)(local_rsp - 0x38) = 0;
    result = WheaReportHwErrorDeviceDriverEx(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007D71A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007D71A0[BB_007D71A0]
  bb_007D71E3[BB_007D71E3]
```
