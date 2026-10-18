# snwscanf_s

- RVA: `0x00505520`–`0x00505559` (길이 `57` bytes)
- VA: `0x0000000140505520`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C389C`
- 디코드: `17`개 명령, `57/57` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0050553F` → [EmpCheckErrataList](../49/EmpCheckErrataList_function_0049E550.md) (function, `0x0049E550`)
- `0x0050554E` → [swinput_s](swinput_s_function_00508DA4.md) (function, `0x00508DA4`)

### Direct callers
- [SiIsWinPeHardDiskZeroUfdBoot](../../page/82/SiIsWinPeHardDiskZeroUfdBoot_function_00828808.md) at `0x0082889C`
- [SiGetBootDeviceName](../../page/A3/SiGetBootDeviceName_function_00A378FC.md) at `0x00A3799D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00505520  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00505525  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0050552A  48 83 EC 48                     sub rsp, 0x48
0050552E  4D 85 C0                        test r8, r8
00505531  75 16                           jne 0x140505549
00505533  4C 21 44 24 20                  and qword ptr [rsp + 0x20], r8
00505538  45 33 C9                        xor r9d, r9d
0050553B  33 D2                           xor edx, edx
0050553D  33 C9                           xor ecx, ecx
0050553F  E8 0C 90 F9 FF                  call 0x14049e550
00505544  83 C8 FF                        or eax, 0xffffffff
00505547  EB 0A                           jmp 0x140505553
00505549  4C 8D 4C 24 68                  lea r9, [rsp + 0x68]
0050554E  E8 51 38 00 00                  call 0x140508da4
00505553  48 83 C4 48                     add rsp, 0x48
00505557  C3                              ret
00505558  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall snwscanf_s(int a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p18 = a3;
    v_stack_p20 = a4;
    v_rsp = (v_rsp) - (72);
    if (a3 != 0) goto loc_00505549;
    a4 = 0;
    a2 = 0;
    a1 = 0;
    result = EmpCheckErrataList(a1, a2, a3, a4);
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    goto loc_00505553;
loc_00505549:
    result = swinput_s(a1, a2, a3, v_stack_p20);
loc_00505553:
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t snwscanf_s(int32_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p18 = Arg3;
    v_stack_p20 = Arg4;
    local_rsp = (local_rsp) - (72);
    if (Arg3 != 0) goto loc_00505549;
    Arg4 = 0;
    Arg2 = 0;
    Arg1 = 0;
    result = EmpCheckErrataList(Arg1, Arg2, Arg3, Arg4);
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    goto loc_00505553;
loc_00505549:
    result = swinput_s(Arg1, Arg2, Arg3, v_stack_p20);
loc_00505553:
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00505520&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00505520[BB_00505520]
  bb_00505533[BB_00505533]
  bb_00505549[BB_00505549]
  bb_00505553[BB_00505553]
  bb_00505558[BB_00505558]
  bb_00505520 -->|branch| bb_00505549
  bb_00505520 -->|fallthrough| bb_00505533
  bb_00505533 -->|branch| bb_00505553
  bb_00505549 -->|flow| bb_00505553
```
