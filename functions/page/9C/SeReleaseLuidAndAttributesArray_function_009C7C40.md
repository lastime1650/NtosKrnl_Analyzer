# SeReleaseLuidAndAttributesArray

- RVA: `0x009C7C40`–`0x009C7C5B` (길이 `27` bytes)
- VA: `0x00000001409C7C40`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009C7C50` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [NtAdjustGroupsToken](NtAdjustGroupsToken_function_009C6640.md) at `0x009C68E7`
- [NtAdjustGroupsToken](NtAdjustGroupsToken_function_009C6640.md) at `0x009C6946`
- [NtAdjustGroupsToken](NtAdjustGroupsToken_function_009C6640.md) at `0x009C69D1`
- [NtAdjustGroupsToken](NtAdjustGroupsToken_function_009C6640.md) at `0x009C6A1F`
- [NtAdjustGroupsToken](NtAdjustGroupsToken_function_009C6640.md) at `0x009C6A2E`
- [NtFilterToken](NtFilterToken_function_009C7890.md) at `0x009C7BE2`
- [NtFilterToken](NtFilterToken_function_009C7890.md) at `0x009C7BF7`
- [NtFilterToken](NtFilterToken_function_009C7890.md) at `0x009C7C0C`
- [NtCreateTokenEx](NtCreateTokenEx_function_009C7C80.md) at `0x009C836D`
- [NtCreateTokenEx](NtCreateTokenEx_function_009C7C80.md) at `0x009C8381`
- [NtCreateTokenEx](NtCreateTokenEx_function_009C7C80.md) at `0x009C8395`
- [NtCreateTokenEx](NtCreateTokenEx_function_009C7C80.md) at `0x009C83EB`
- [NtCreateTokenEx](NtCreateTokenEx_function_009C7C80.md) at `0x009C8433`
- [NtCreateTokenEx](NtCreateTokenEx_function_009C7C80.md) at `0x009C8448`
- [NtCreateTokenEx](NtCreateTokenEx_function_009C7C80.md) at `0x009C845D`
- [NtCreateTokenEx](NtCreateTokenEx_function_009C7C80.md) at `0x009C8692`
- [NtAdjustPrivilegesToken](NtAdjustPrivilegesToken_function_009C86C0.md) at `0x009C896F`
- [NtAdjustPrivilegesToken](NtAdjustPrivilegesToken_function_009C86C0.md) at `0x009C8A38`
- [NtAdjustPrivilegesToken](NtAdjustPrivilegesToken_function_009C86C0.md) at `0x009C8AC1`
- [NtAdjustPrivilegesToken](NtAdjustPrivilegesToken_function_009C86C0.md) at `0x009C8ACB`
- [NtPrivilegeCheck](NtPrivilegeCheck_function_009C8AE0.md) at `0x009C8CC9`
- [NtCreateLowBoxToken](../AB/NtCreateLowBoxToken_function_00AB9880.md) at `0x00AB9B39`
- [NtCreateLowBoxToken](../AB/NtCreateLowBoxToken_function_00AB9880.md) at `0x00ABA3A8`
- [NtSetInformationToken](../AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF1970`
- [NtSetInformationToken](../AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF1EBA`
- [sub_00B30BB4](../B3/Unknown_function_00B30BB4.md) at `0x00B30C2D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x009C7C50` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009C7C40  48 83 EC 28                     sub rsp, 0x28
009C7C44  80 FA 01                        cmp dl, 1
009C7C47  77 0C                           ja 0x1409c7c55
009C7C49  48 85 C9                        test rcx, rcx
009C7C4C  74 07                           je 0x1409c7c55
009C7C4E  33 D2                           xor edx, edx
009C7C50  E8 1B AC 1B 00                  call 0x140b82870
009C7C55  48 83 C4 28                     add rsp, 0x28
009C7C59  C3                              ret
009C7C5A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeReleaseLuidAndAttributesArray(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((unsigned __int8)(a2)) > 1) goto loc_009C7C55;
    if (a1 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SeReleaseLuidAndAttributesArray(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((uint8_t)(Arg2)) > 1) goto loc_009C7C55;
    if (Arg1 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009C7C40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009C7C40[BB_009C7C40]
  bb_009C7C49[BB_009C7C49]
  bb_009C7C4E[BB_009C7C4E]
  bb_009C7C55[BB_009C7C55]
  bb_009C7C5A[BB_009C7C5A]
  bb_009C7C40 -->|branch| bb_009C7C55
  bb_009C7C40 -->|fallthrough| bb_009C7C49
  bb_009C7C49 -->|branch| bb_009C7C55
  bb_009C7C49 -->|fallthrough| bb_009C7C4E
  bb_009C7C4E -->|flow| bb_009C7C55
```
