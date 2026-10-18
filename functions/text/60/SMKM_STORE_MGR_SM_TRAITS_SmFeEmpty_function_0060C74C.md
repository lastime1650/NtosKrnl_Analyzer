# SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmFeEmpty

- RVA: `0x0060C74C`–`0x0060C79E` (길이 `82` bytes)
- VA: `0x000000014060C74C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `21`개 명령, `82/82` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0060C763` → [StLockAcquireExclusive](../26/StLockAcquireExclusive_function_00266FF0.md) (function, `0x00266FF0`)
- `0x0060C77B` → [B_TREE<_SM_PAGE_KEY,SMKM_STORE_MGR<SM_TRAITS>::SMKM_FRONTEND_ENTRY,4096,B_TREE_DUMMY_NODE_POOL,B_TREE_KEY_COMPARATOR<_SM_PAGE_KEY> >::BTreeNodeFree](B_TREE__SM_PAGE_KEY_SMKM_STORE_MGR_SM_TRAITS_SMKM_FRONTEND_ENTRY_4096_B_TREE_DUMMY_NODE_POOL_B_TREE__function_0060BC94.md) (function, `0x0060BC94`)
- `0x0060C78D` → [StLockReleaseExclusive](../26/StLockReleaseExclusive_function_00267050.md) (function, `0x00267050`)

### Direct callers
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmStoreMgrCallback](../3B/SMKM_STORE_MGR_SM_TRAITS_SmStoreMgrCallback_function_003B0040.md) at `0x003B00D0`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0060C74C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0060C751  57                              push rdi
0060C752  48 83 EC 20                     sub rsp, 0x20
0060C756  48 8D B9 B8 01 00 00            lea rdi, [rcx + 0x1b8]
0060C75D  48 8B D9                        mov rbx, rcx
0060C760  48 8B CF                        mov rcx, rdi
0060C763  E8 88 A8 C5 FF                  call 0x140266ff0
0060C768  48 8B 93 C0 01 00 00            mov rdx, qword ptr [rbx + 0x1c0]
0060C76F  48 85 D2                        test rdx, rdx
0060C772  74 0C                           je 0x14060c780
0060C774  48 8D 8B C0 01 00 00            lea rcx, [rbx + 0x1c0]
0060C77B  E8 14 F5 FF FF                  call 0x14060bc94
0060C780  0F 57 C0                        xorps xmm0, xmm0
0060C783  48 8B CF                        mov rcx, rdi
0060C786  0F 11 83 C0 01 00 00            movups xmmword ptr [rbx + 0x1c0], xmm0
0060C78D  E8 BE A8 C5 FF                  call 0x140267050
0060C792  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0060C797  48 83 C4 20                     add rsp, 0x20
0060C79B  5F                              pop rdi
0060C79C  C3                              ret
0060C79D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SMKM_STORE_MGR_SM_TRAITS___SmFeEmpty(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = StLockAcquireExclusive(a1 + 440, a2, a3, a4);
    if (*(unsigned __int64 *)(a1 + 448) != 0) {
        a1 = a1 + 448;
        result = B_TREE__SM_PAGE_KEY_SMKM_STORE_MGR_SM_TRAITS___SMKM_FRONTEND_ENTRY_4096_B_TREE_DUMMY_NODE_POOL_B_TRE(a1, *(unsigned __int64 *)(a1 + 448), a3, a4);
    }
    *(unsigned __int64 *)(a1 + 448) = v_xmm0;
    result = StLockReleaseExclusive(a1 + 440, *(unsigned __int64 *)(a1 + 448), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SMKM_STORE_MGR_SM_TRAITS___SmFeEmpty(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = StLockAcquireExclusive(Arg1 + 440, a2, a3, a4);
    if (*(uint64_t *)(arg1 + 0x1C0) != 0) {
        Arg1 = Arg1 + 448;
        result = B_TREE__SM_PAGE_KEY_SMKM_STORE_MGR_SM_TRAITS___SMKM_FRONTEND_ENTRY_4096_B_TREE_DUMMY_NODE_POOL_B_TRE(Arg1, *(uint64_t *)(arg1 + 0x1C0), a3, a4);
    }
    *(uint64_t *)(arg1 + 0x1C0) = v_xmm0;
    result = StLockReleaseExclusive(Arg1 + 440, *(uint64_t *)(arg1 + 0x1C0), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1B8` | `64` | `R` |
| `Arg1` | `+ 0x1C0` | `64` | `R` |
| `Arg1` | `+ 0x1C0` | `128` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0060C74C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0060C74C[BB_0060C74C]
  bb_0060C774[BB_0060C774]
  bb_0060C780[BB_0060C780]
  bb_0060C79D[BB_0060C79D]
  bb_0060C74C -->|branch| bb_0060C780
  bb_0060C74C -->|fallthrough| bb_0060C774
  bb_0060C774 -->|flow| bb_0060C780
```
