# SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmTrimWsStore

- RVA: `0x004BEB1C`–`0x004BEB43` (길이 `39` bytes)
- VA: `0x00000001404BEB1C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `12`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004BEB31` → [SMKM_STORE<SM_TRAITS>::SmStTrimWsStore](SMKM_STORE_SM_TRAITS_SmStTrimWsStore_function_004BEB4C.md) (function, `0x004BEB4C`)

### Direct callers
- [SmStoreCompressionStop](../../page/A6/SmStoreCompressionStop_function_00A6197C.md) at `0x00A61AB8`
- [SmProcessSystemStoreTrimRequest](../../page/A7/SmProcessSystemStoreTrimRequest_function_00A784E0.md) at `0x00A78762`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004BEB1C  48 83 EC 28                     sub rsp, 0x28
004BEB20  F7 02 00 00 02 00               test dword ptr [rdx], 0x20000
004BEB26  4C 8B CA                        mov r9, rdx
004BEB29  74 11                           je 0x1404beb3c
004BEB2B  49 8B D0                        mov rdx, r8
004BEB2E  49 8B C9                        mov rcx, r9
004BEB31  E8 16 00 00 00                  call 0x1404beb4c
004BEB36  48 83 C4 28                     add rsp, 0x28
004BEB3A  C3                              ret
004BEB3B  CC                              int3
004BEB3C  B8 BB 00 00 C0                  mov eax, 0xc00000bb
004BEB41  EB F3                           jmp 0x1404beb36
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SMKM_STORE_MGR_SM_TRAITS___SmTrimWsStore(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((*(unsigned int *)(a2)) & (0x20000ULL)) == 0) goto loc_004BEB3C;
    result = SMKM_STORE_SM_TRAITS___SmStTrimWsStore(a2, a3, a3, a2);
loc_004BEB36:
    v_rsp = (v_rsp) + (40);
    return result;
loc_004BEB3C:
    goto loc_004BEB36;
}
```

## 5. (Beta) C Style

```c
int64_t SMKM_STORE_MGR_SM_TRAITS___SmTrimWsStore(int64_t Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((*(uint32_t *)(arg2)) & (0x20000ULL)) == 0) goto loc_004BEB3C;
    result = SMKM_STORE_SM_TRAITS___SmStTrimWsStore(Arg2, Arg3, Arg3, Arg2);
loc_004BEB36:
    local_rsp = (local_rsp) + (40);
    return result;
loc_004BEB3C:
    goto loc_004BEB36;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004BEB1C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004BEB1C[BB_004BEB1C]
  bb_004BEB2B[BB_004BEB2B]
  bb_004BEB36[BB_004BEB36]
  bb_004BEB3B[BB_004BEB3B]
  bb_004BEB3C[BB_004BEB3C]
  bb_004BEB1C -->|branch| bb_004BEB3C
  bb_004BEB1C -->|fallthrough| bb_004BEB2B
  bb_004BEB2B -->|flow| bb_004BEB36
  bb_004BEB3B -->|flow| bb_004BEB3C
  bb_004BEB3C -->|branch| bb_004BEB36
```
