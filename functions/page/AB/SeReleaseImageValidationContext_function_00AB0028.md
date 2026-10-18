# SeReleaseImageValidationContext

- RVA: `0x00AB0028`–`0x00AB004C` (길이 `36` bytes)
- VA: `0x0000000140AB0028`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `11`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AB003A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AB0045` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [MiDeleteControlArea](../../text/36/MiDeleteControlArea_function_003691F4.md) at `0x0036931C`
- [sub_00B2542C](../B2/Unknown_function_00B2542C.md) at `0x00B254E0`

### Static image references
- `0x00AB002C` → RVA `0x00F04EA8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00AB003A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AB0045` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB0028  48 83 EC 28                     sub rsp, 0x28
00AB002C  48 8B 05 75 4E 45 00            mov rax, qword ptr [rip + 0x454e75]
00AB0033  48 85 C0                        test rax, rax
00AB0036  75 0D                           jne 0x140ab0045
00AB0038  33 D2                           xor edx, edx
00AB003A  E8 31 28 0D 00                  call 0x140b82870
00AB003F  48 83 C4 28                     add rsp, 0x28
00AB0043  C3                              ret
00AB0044  CC                              int3
00AB0045  E8 86 AA C0 FF                  call 0x1406baad0
00AB004A  EB F3                           jmp 0x140ab003f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeReleaseImageValidationContext(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(v_rip + 4542069) != 0) goto loc_00AB0045;
    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, a3, a4);
loc_00AB003F:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00AB0045:
    result = guard_dispatch_icall(a1, a2, a3, a4);
    goto loc_00AB003F;
}
```

## 5. (Beta) C Style

```c
int64_t SeReleaseImageValidationContext(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(v_rip + 0x454E75) != 0) goto loc_00AB0045;
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
loc_00AB003F:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00AB0045:
    result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    goto loc_00AB003F;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB0028&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AB0028[BB_00AB0028]
  bb_00AB0038[BB_00AB0038]
  bb_00AB003F[BB_00AB003F]
  bb_00AB0044[BB_00AB0044]
  bb_00AB0045[BB_00AB0045]
  bb_00AB0028 -->|branch| bb_00AB0045
  bb_00AB0028 -->|fallthrough| bb_00AB0038
  bb_00AB0038 -->|flow| bb_00AB003F
  bb_00AB0044 -->|flow| bb_00AB0045
  bb_00AB0045 -->|branch| bb_00AB003F
```
