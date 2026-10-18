# IoSetDeviceInterfaceState

- RVA: `0x00950740`–`0x009507AB` (길이 `107` bytes)
- VA: `0x0000000140950740`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BE4`
- 디코드: `31`개 명령, `107/107` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0095076A` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00950778` → [IopProcessSetInterfaceState](IopProcessSetInterfaceState_function_00950964.md) (function, `0x00950964`)
- `0x00950786` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x0095078B` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- [DifIoSetDeviceInterfaceStateWrapper](../../text/62/DifIoSetDeviceInterfaceStateWrapper_function_0062CCC0.md) at `0x0062CD94`
- [PiSwDeviceInterfacesUpdateState](../94/PiSwDeviceInterfacesUpdateState_function_0094E744.md) at `0x0094E7DF`
- [PiSwDeviceInterfaceSetState](../94/PiSwDeviceInterfaceSetState_function_0094ED48.md) at `0x0094EE0C`
- [sub_00B34868](../B3/Unknown_function_00B34868.md) at `0x00B34882`

### Static image references
- `0x0095075B` → RVA `0x00F8C600` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0095076A` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00950786` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x0095078B` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00950740  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00950745  57                              push rdi
00950746  48 83 EC 20                     sub rsp, 0x20
0095074A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00950753  40 8A FA                        mov dil, dl
00950756  48 8B D9                        mov rbx, rcx
00950759  B2 01                           mov dl, 1
0095075B  48 8D 0D 9E BE 63 00            lea rcx, [rip + 0x63be9e]
00950762  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00950769  90                              nop
0095076A  E8 B1 46 8C FF                  call 0x140214e20
0095076F  41 B0 01                        mov r8b, 1
00950772  40 8A D7                        mov dl, dil
00950775  48 8B CB                        mov rcx, rbx
00950778  E8 E7 01 00 00                  call 0x140950964
0095077D  48 8D 0D 7C BE 63 00            lea rcx, [rip + 0x63be7c]
00950784  8B D8                           mov ebx, eax
00950786  E8 85 F2 90 FF                  call 0x14025fa10
0095078B  E8 20 D1 90 FF                  call 0x14025d8b0
00950790  85 DB                           test ebx, ebx
00950792  78 0E                           js 0x1409507a2
00950794  8B C3                           mov eax, ebx
00950796  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0095079B  48 83 C4 20                     add rsp, 0x20
0095079F  5F                              pop rdi
009507A0  C3                              ret
009507A1  CC                              int3
009507A2  40 F6 DF                        neg dil
009507A5  1B C9                           sbb ecx, ecx
009507A7  23 D9                           and ebx, ecx
009507A9  EB E9                           jmp 0x140950794
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoSetDeviceInterfaceState(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = ExAcquireResourceExclusiveLite(v_rip + 6536862, 1, a3, a4);
    result = IopProcessSetInterfaceState(a1, a2, 1, a4);
    result = ExReleaseResourceLite(v_rip + 6536828, a2, 1, a4);
    result = KeLeaveCriticalRegion(v_rip + 6536828, a2, 1, a4);
    if (sign_flag) goto loc_009507A2;
loc_00950794:
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_009507A2:
    v_rdi = (unsigned __int8)(-(a2));
    v_rbx = (unsigned int)((v_stack_p8) & ((unsigned int)(v_rip + 6536828)));
    goto loc_00950794;
}
```

## 5. (Beta) C Style

```c
int64_t IoSetDeviceInterfaceState(int64_t Arg1, uint8_t Arg2)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = ExAcquireResourceExclusiveLite(v_rip + 6536862, 1, a3, a4);
    result = IopProcessSetInterfaceState(Arg1, Arg2, 1, a4);
    result = ExReleaseResourceLite(v_rip + 6536828, Arg2, 1, a4);
    result = KeLeaveCriticalRegion(v_rip + 6536828, Arg2, 1, a4);
    if (sign_flag) goto loc_009507A2;
loc_00950794:
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_009507A2:
    local_rdi = (uint8_t)(-(Arg2));
    local_rbx = (uint32_t)((v_stack_p8) & ((uint32_t)(v_rip + 6536828)));
    goto loc_00950794;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00950740&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00950740[BB_00950740]
  bb_00950794[BB_00950794]
  bb_009507A1[BB_009507A1]
  bb_009507A2[BB_009507A2]
  bb_00950740 -->|branch| bb_009507A2
  bb_00950740 -->|fallthrough| bb_00950794
  bb_009507A1 -->|flow| bb_009507A2
  bb_009507A2 -->|branch| bb_00950794
```
