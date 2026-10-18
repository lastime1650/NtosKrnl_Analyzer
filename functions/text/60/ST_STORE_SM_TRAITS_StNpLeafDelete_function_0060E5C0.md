# ST_STORE&lt;SM_TRAITS&gt;::StNpLeafDelete

- RVA: `0x0060E5C0`–`0x0060E600` (길이 `64` bytes)
- VA: `0x000000014060E5C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `16`개 명령, `64/64` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0060E5F5` → [ST_STORE<SM_TRAITS>::StDmPageRemove](../20/ST_STORE_SM_TRAITS_StDmPageRemove_function_002049A0.md) (function, `0x002049A0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0060E5C0  48 83 EC 48                     sub rsp, 0x48
0060E5C4  48 8B 09                        mov rcx, qword ptr [rcx]
0060E5C7  83 E2 FC                        and edx, 0xfffffffc
0060E5CA  83 64 24 24 00                  and dword ptr [rsp + 0x24], 0
0060E5CF  B8 01 00 00 00                  mov eax, 1
0060E5D4  0F 57 C0                        xorps xmm0, xmm0
0060E5D7  89 54 24 28                     mov dword ptr [rsp + 0x28], edx
0060E5DB  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
0060E5E0  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0060E5E4  48 8B 89 80 00 00 00            mov rcx, qword ptr [rcx + 0x80]
0060E5EB  F3 0F 7F 44 24 30               movdqu xmmword ptr [rsp + 0x30], xmm0
0060E5F1  89 44 24 2C                     mov dword ptr [rsp + 0x2c], eax
0060E5F5  E8 A6 63 BF FF                  call 0x1402049a0
0060E5FA  48 83 C4 48                     add rsp, 0x48
0060E5FE  C3                              ret
0060E5FF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ST_STORE_SM_TRAITS___StNpLeafDelete(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;
    unsigned int v_stack_m24;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (72);
    a2 = (unsigned int)((a2) & (0xFFFFFFFCULL));
    v_stack_m20 = a2;
    v_stack_m28 = 1;
    v_stack_m18 = v_xmm0;
    v_stack_m1C = 1;
    result = ST_STORE_SM_TRAITS___StDmPageRemove(*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 128), v_stack_m28, a3, a4);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ST_STORE_SM_TRAITS___StNpLeafDelete(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;
    uint32_t v_stack_m24;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    Arg2 = (uint32_t)((Arg2) & (0xFFFFFFFCULL));
    v_stack_m20 = Arg2;
    v_stack_m28 = 1;
    v_stack_m18 = v_xmm0;
    v_stack_m1C = 1;
    result = ST_STORE_SM_TRAITS___StDmPageRemove(*(uint64_t *)(*(uint64_t *)(arg1) + 0x80), v_stack_m28, a3, a4);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0060E5C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0060E5C0[BB_0060E5C0]
  bb_0060E5FF[BB_0060E5FF]
```
