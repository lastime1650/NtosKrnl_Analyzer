# SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmStoreRequestEx

- RVA: `0x004A21D8`–`0x004A2213` (길이 `59` bytes)
- VA: `0x00000001404A21D8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005DDFC`
- 디코드: `18`개 명령, `59/59` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004A2201` → [SMKM_STORE<SM_TRAITS>::SmStWorkItemQueue](../31/SMKM_STORE_SM_TRAITS_SmStWorkItemQueue_function_00317A34.md) (function, `0x00317A34`)

### Direct callers
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmStoreRequest](SMKM_STORE_MGR_SM_TRAITS_SmStoreRequest_function_004A2160.md) at `0x004A219C`
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmStoreContentsRundown](../61/SMKM_STORE_MGR_SM_TRAITS_SmStoreContentsRundown_function_00610ADC.md) at `0x00610B6E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004A21D8  48 83 EC 28                     sub rsp, 0x28
004A21DC  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
004A21E1  4D 8B D0                        mov r10, r8
004A21E4  4C 8B DA                        mov r11, rdx
004A21E7  48 85 C0                        test rax, rax
004A21EA  74 25                           je 0x1404a2211
004A21EC  48 83 60 08 00                  and qword ptr [rax + 8], 0
004A21F1  4C 89 08                        mov qword ptr [rax], r9
004A21F4  49 89 40 20                     mov qword ptr [r8 + 0x20], rax
004A21F8  49 8B D2                        mov rdx, r10
004A21FB  45 33 C0                        xor r8d, r8d
004A21FE  49 8B CB                        mov rcx, r11
004A2201  E8 2E 58 E7 FF                  call 0x140317a34
004A2206  B8 03 01 00 00                  mov eax, 0x103
004A220B  48 83 C4 28                     add rsp, 0x28
004A220F  C3                              ret
004A2210  CC                              int3
004A2211  EB E1                           jmp 0x1404a21f4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SMKM_STORE_MGR_SM_TRAITS___SmStoreRequestEx(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a5 == 0) goto loc_004A2211;
    *(unsigned __int64 *)(a5) = a4;
loc_004A21F4:
    *(unsigned __int64 *)(a3 + 32) = a5;
    a3 = 0;
    result = SMKM_STORE_SM_TRAITS___SmStWorkItemQueue(a2, a3, a3, a4);
    v_rsp = (v_rsp) + (40);
    return 259;
loc_004A2211:
    goto loc_004A21F4;
}
```

## 5. (Beta) C Style

```c
int64_t SMKM_STORE_MGR_SM_TRAITS___SmStoreRequestEx(int64_t Arg1, int64_t Arg2, void *Arg3, int64_t Arg4, int64_t Arg5)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg5 == 0) goto loc_004A2211;
    *(uint64_t *)(Arg5) = Arg4;
loc_004A21F4:
    *(uint64_t *)(arg3 + 0x20) = Arg5;
    Arg3 = 0;
    result = SMKM_STORE_SM_TRAITS___SmStWorkItemQueue(Arg2, Arg3, Arg3, Arg4);
    local_rsp = (local_rsp) + (40);
    return 259;
loc_004A2211:
    goto loc_004A21F4;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x20` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004A21D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004A21D8[BB_004A21D8]
  bb_004A21EC[BB_004A21EC]
  bb_004A21F4[BB_004A21F4]
  bb_004A2210[BB_004A2210]
  bb_004A2211[BB_004A2211]
  bb_004A21D8 -->|branch| bb_004A2211
  bb_004A21D8 -->|fallthrough| bb_004A21EC
  bb_004A21EC -->|flow| bb_004A21F4
  bb_004A2210 -->|flow| bb_004A2211
  bb_004A2211 -->|branch| bb_004A21F4
```
