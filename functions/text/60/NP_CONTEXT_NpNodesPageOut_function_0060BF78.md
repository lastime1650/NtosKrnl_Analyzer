# NP_CONTEXT::NpNodesPageOut

- RVA: `0x0060BF78`–`0x0060BF98` (길이 `32` bytes)
- VA: `0x000000014060BF78`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0060BF89` → [NP_CONTEXT::NpiPerformPageOut](NP_CONTEXT_NpiPerformPageOut_function_0060C0BC.md) (function, `0x0060C0BC`)

### Direct callers
- [ST_STORE&lt;SM_TRAITS&gt;::StMetaRegionsUpdate](../4C/ST_STORE_SM_TRAITS_StMetaRegionsUpdate_function_004C1DFC.md) at `0x004C1F10`
- [ST_STORE&lt;SM_TRAITS&gt;::StMetaRegionsUpdate](../4C/ST_STORE_SM_TRAITS_StMetaRegionsUpdate_function_004C1DFC.md) at `0x004C1F2C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0060BF78  48 83 EC 28                     sub rsp, 0x28
0060BF7C  48 8B D1                        mov rdx, rcx
0060BF7F  48 8B 09                        mov rcx, qword ptr [rcx]
0060BF82  8B 01                           mov eax, dword ptr [rcx]
0060BF84  39 41 28                        cmp dword ptr [rcx + 0x28], eax
0060BF87  76 07                           jbe 0x14060bf90
0060BF89  E8 2E 01 00 00                  call 0x14060c0bc
0060BF8E  EB 02                           jmp 0x14060bf92
0060BF90  33 C0                           xor eax, eax
0060BF92  48 83 C4 28                     add rsp, 0x28
0060BF96  C3                              ret
0060BF97  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NP_CONTEXT__NpNodesPageOut(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1) + 40)) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1)))))) goto loc_0060BF90;
    result = NP_CONTEXT__NpiPerformPageOut(*(unsigned __int64 *)(a1), a1, a3, a4);
    goto loc_0060BF92;
loc_0060BF90:
    result = 0;
loc_0060BF92:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NP_CONTEXT__NpNodesPageOut(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint32_t *)(*(uint64_t *)(arg1) + 0x28)) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1)))))) goto loc_0060BF90;
    result = NP_CONTEXT__NpiPerformPageOut(*(uint64_t *)(arg1), Arg1, a3, a4);
    goto loc_0060BF92;
loc_0060BF90:
    result = 0;
loc_0060BF92:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0060BF78&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0060BF78[BB_0060BF78]
  bb_0060BF89[BB_0060BF89]
  bb_0060BF90[BB_0060BF90]
  bb_0060BF92[BB_0060BF92]
  bb_0060BF97[BB_0060BF97]
  bb_0060BF78 -->|branch| bb_0060BF90
  bb_0060BF78 -->|fallthrough| bb_0060BF89
  bb_0060BF89 -->|branch| bb_0060BF92
  bb_0060BF90 -->|flow| bb_0060BF92
```
