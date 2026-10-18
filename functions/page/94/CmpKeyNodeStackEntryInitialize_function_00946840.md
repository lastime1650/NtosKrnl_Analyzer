# CmpKeyNodeStackEntryInitialize

- RVA: `0x00946840`–`0x00946861` (길이 `33` bytes)
- VA: `0x0000000140946840`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00946856` → [HvpGetCellContextInitialize](../85/HvpGetCellContextInitialize_function_00855F10.md) (function, `0x00855F10`)

### Direct callers
- [CmpGetSubKeyCountForKcbStack](CmpGetSubKeyCountForKcbStack_function_00944628.md) at `0x0094466A`
- [CmpPromoteSingleKeyFromKcbStacks](CmpPromoteSingleKeyFromKcbStacks_function_009446E8.md) at `0x00944744`
- [CmpPromoteSingleKeyFromKcbStacks](CmpPromoteSingleKeyFromKcbStacks_function_009446E8.md) at `0x0094476B`
- [CmpValueEnumStackStartFromKcbStack](CmpValueEnumStackStartFromKcbStack_function_00944AA4.md) at `0x00944AEF`
- [CmpKeyEnumStackStartFromKcbStack](CmpKeyEnumStackStartFromKcbStack_function_00944F18.md) at `0x00944F70`
- [CmpKeyNodeStackEntryReset](CmpKeyNodeStackEntryReset_function_009467E0.md) at `0x009467F1`
- [CmpInitializeKeyNodeStack](CmpInitializeKeyNodeStack_function_00946804.md) at `0x00946824`
- [sub_00B255A6](../B2/Unknown_function_00B255A6.md) at `0x00B255AD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00946840  48 83 EC 28                     sub rsp, 0x28
00946844  0F 57 C0                        xorps xmm0, xmm0
00946847  0F 11 01                        movups xmmword ptr [rcx], xmm0
0094684A  0F 11 41 10                     movups xmmword ptr [rcx + 0x10], xmm0
0094684E  83 49 08 FF                     or dword ptr [rcx + 8], 0xffffffff
00946852  48 83 C1 18                     add rcx, 0x18
00946856  E8 B5 F6 F0 FF                  call 0x140855f10
0094685B  48 83 C4 28                     add rsp, 0x28
0094685F  C3                              ret
00946860  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpKeyNodeStackEntryInitialize(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    *(unsigned __int64 *)(a1) = v_xmm0;
    *(unsigned __int64 *)(a1 + 16) = v_xmm0;
    a1 = (a1) + (24);
    result = HvpGetCellContextInitialize(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpKeyNodeStackEntryInitialize(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    *(uint64_t *)(arg1) = v_xmm0;
    *(uint64_t *)(arg1 + 0x10) = v_xmm0;
    Arg1 = (Arg1) + (24);
    result = HvpGetCellContextInitialize(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R/W` |
| `Arg1` | `+ 0x10` | `128` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00946840&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00946840[BB_00946840]
  bb_00946860[BB_00946860]
```
