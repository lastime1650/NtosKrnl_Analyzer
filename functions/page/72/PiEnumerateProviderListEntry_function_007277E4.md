# PiEnumerateProviderListEntry

- RVA: `0x007277E4`–`0x0072780E` (길이 `42` bytes)
- VA: `0x00000001407277E4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007277ED` → [PiListEntryToDependencyEdge](../../text/4F/PiListEntryToDependencyEdge_function_004F9648.md) (function, `0x004F9648`)

### Direct callers
- [PipCheckIfAllProvidersHaveDevnodes](../6F/PipCheckIfAllProvidersHaveDevnodes_function_006FF944.md) at `0x006FF989`
- [IopCheckIfMergeRequired](../A0/IopCheckIfMergeRequired_function_00A061B4.md) at `0x00A0626E`
- [IopSortRelationListForRemove](../A0/IopSortRelationListForRemove_function_00A06C30.md) at `0x00A06D71`
- [PipCheckForUnsatisfiedDependencies](../A0/PipCheckForUnsatisfiedDependencies_function_00A06E44.md) at `0x00A06EB0`
- [PiQueryPowerDependencyRelations](../AA/PiQueryPowerDependencyRelations_function_00AA4524.md) at `0x00AA45B0`
- [PiQueryPowerDependencyRelations](../AA/PiQueryPowerDependencyRelations_function_00AA4524.md) at `0x00AA466B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007277ED` → [PiListEntryToDependencyEdge](../../text/4F/PiListEntryToDependencyEdge_function_004F9648.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007277E4  48 83 EC 28                     sub rsp, 0x28
007277E8  4C 8B D2                        mov r10, rdx
007277EB  33 D2                           xor edx, edx
007277ED  E8 56 1E DD FF                  call 0x1404f9648
007277F2  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
007277F6  4C 8B 49 30                     mov r9, qword ptr [rcx + 0x30]
007277FA  4D 89 0A                        mov qword ptr [r10], r9
007277FD  4D 85 C0                        test r8, r8
00727800  74 06                           je 0x140727808
00727802  8B 40 30                        mov eax, dword ptr [rax + 0x30]
00727805  41 89 00                        mov dword ptr [r8], eax
00727808  48 83 C4 28                     add rsp, 0x28
0072780C  C3                              ret
0072780D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiEnumerateProviderListEntry(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = 0;
    result = PiListEntryToDependencyEdge(a1, a2, a3, a4);
    *(unsigned __int64 *)(a2) = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 48);
    if (a3 != 0) {
        result = *(unsigned int *)(result + 48);
        *(unsigned int *)(a3) = (unsigned int)(result);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiEnumerateProviderListEntry(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = 0;
    result = PiListEntryToDependencyEdge(Arg1, Arg2, Arg3, a4);
    *(uint64_t *)(Arg2) = *(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x30);
    if (Arg3 != 0) {
        result = *(uint32_t *)(result + 0x30);
        *(uint32_t *)(Arg3) = (uint32_t)(result);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007277E4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007277E4[BB_007277E4]
  bb_00727802[BB_00727802]
  bb_00727808[BB_00727808]
  bb_0072780D[BB_0072780D]
  bb_007277E4 -->|branch| bb_00727808
  bb_007277E4 -->|fallthrough| bb_00727802
  bb_00727802 -->|flow| bb_00727808
```
