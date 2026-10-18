# SMKM_STORE&lt;SM_TRAITS&gt;::SmStMapRegion

- RVA: `0x0034D738`–`0x0034D75F` (길이 `39` bytes)
- VA: `0x000000014034D738`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000789BC`
- 디코드: `11`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0034D74D` → [SMKM_STORE<SM_TRAITS>::SmStMapVirtualRegion](SMKM_STORE_SM_TRAITS_SmStMapVirtualRegion_function_0034D770.md) (function, `0x0034D770`)
- `0x0034D758` → [SMKM_STORE<SM_TRAITS>::SmStMapPhysicalRegion](../60/SMKM_STORE_SM_TRAITS_SmStMapPhysicalRegion_function_0060CB6C.md) (function, `0x0060CB6C`)

### Direct callers
- [sub_0034CBFD](Unknown_function_0034CBFD.md) at `0x0034CC24`
- [ST_STORE&lt;SM_TRAITS&gt;::StMapAndLockRegion](../4E/ST_STORE_SM_TRAITS_StMapAndLockRegion_function_004EC090.md) at `0x004EC165`
- [ST_STORE&lt;SM_TRAITS&gt;::StMapAndLockRegion](../4E/ST_STORE_SM_TRAITS_StMapAndLockRegion_function_004EC090.md) at `0x004EC210`
- [sub_006F84D2](../6F/Unknown_function_006F84D2.md) at `0x006F8595`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0034D738  48 83 EC 38                     sub rsp, 0x38
0034D73C  F6 81 95 1A 00 00 04            test byte ptr [rcx + 0x1a95], 4
0034D743  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
0034D747  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0034D74B  74 0B                           je 0x14034d758
0034D74D  E8 1E 00 00 00                  call 0x14034d770
0034D752  48 83 C4 38                     add rsp, 0x38
0034D756  C3                              ret
0034D757  CC                              int3
0034D758  E8 0F F4 2B 00                  call 0x14060cb6c
0034D75D  EB F3                           jmp 0x14034d752
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SMKM_STORE_SM_TRAITS___SmStMapRegion(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;

    v_rsp = (v_rsp) - (56);
    v_stack_m18 = (unsigned int)((unsigned int)(a5));
    if (((*(unsigned __int8 *)(a1 + 6805)) & (4)) == 0) goto loc_0034D758;
    result = SMKM_STORE_SM_TRAITS___SmStMapVirtualRegion(a1, a2, a3, a4);
loc_0034D752:
    v_rsp = (v_rsp) + (56);
    return result;
loc_0034D758:
    result = SMKM_STORE_SM_TRAITS___SmStMapPhysicalRegion(a1, a2, a3, a4);
    goto loc_0034D752;
}
```

## 5. (Beta) C Style

```c
int64_t SMKM_STORE_SM_TRAITS___SmStMapRegion(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    v_stack_m18 = (uint32_t)((uint32_t)(Arg5));
    if (((*(uint8_t *)(arg1 + 0x1A95)) & (4)) == 0) goto loc_0034D758;
    result = SMKM_STORE_SM_TRAITS___SmStMapVirtualRegion(Arg1, Arg2, Arg3, Arg4);
loc_0034D752:
    local_rsp = (local_rsp) + (56);
    return result;
loc_0034D758:
    result = SMKM_STORE_SM_TRAITS___SmStMapPhysicalRegion(Arg1, Arg2, Arg3, Arg4);
    goto loc_0034D752;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1A95` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0034D738&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0034D738[BB_0034D738]
  bb_0034D74D[BB_0034D74D]
  bb_0034D752[BB_0034D752]
  bb_0034D757[BB_0034D757]
  bb_0034D758[BB_0034D758]
  bb_0034D738 -->|branch| bb_0034D758
  bb_0034D738 -->|fallthrough| bb_0034D74D
  bb_0034D74D -->|flow| bb_0034D752
  bb_0034D757 -->|flow| bb_0034D758
  bb_0034D758 -->|branch| bb_0034D752
```
