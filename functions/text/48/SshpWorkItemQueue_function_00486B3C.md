# SshpWorkItemQueue

- RVA: `0x00486B3C`–`0x00486B67` (길이 `43` bytes)
- VA: `0x0000000140486B3C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00486B5C` → [ExQueueWorkItem](../2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)

### Direct callers
- [SshpDereferenceBlocker](SshpDereferenceBlocker_function_00486960.md) at `0x00486AD3`
- [SshpSessionManagerOpenControlTrace](../../page/77/SshpSessionManagerOpenControlTrace_function_007744C0.md) at `0x0077465A`
- [SshpSessionManagerSendControlEventSlimEtl](../../page/A8/SshpSessionManagerSendControlEventSlimEtl_function_00A87200.md) at `0x00A87346`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00486B3C  48 83 EC 28                     sub rsp, 0x28
00486B40  0F 0D 49 20                     prefetchw byte ptr [rcx + 0x20]
00486B44  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
00486B47  8B D0                           mov edx, eax
00486B49  83 CA 03                        or edx, 3
00486B4C  F0 0F B1 51 20                  lock cmpxchg dword ptr [rcx + 0x20], edx
00486B51  75 F4                           jne 0x140486b47
00486B53  BA 01 00 00 00                  mov edx, 1
00486B58  84 C2                           test dl, al
00486B5A  75 05                           jne 0x140486b61
00486B5C  E8 BF 29 E7 FF                  call 0x1402f9520
00486B61  48 83 C4 28                     add rsp, 0x28
00486B65  C3                              ret
00486B66  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SshpWorkItemQueue(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
loc_00486B47:
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32))))) | (3));
    if (condition_is_not_equal) goto loc_00486B47;
    result = (unsigned int)(*(unsigned int *)(a1 + 32));
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 32))))) == 0) {
        result = ExQueueWorkItem(a1, 1, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SshpWorkItemQueue(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
loc_00486B47:
    a2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20))))) | (3));
    if (condition_is_not_equal) goto loc_00486B47;
    result = (uint32_t)(*(uint32_t *)(arg1 + 0x20));
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20))))) == 0) {
        result = ExQueueWorkItem(Arg1, 1, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `8` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00486B3C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00486B3C[BB_00486B3C]
  bb_00486B47[BB_00486B47]
  bb_00486B53[BB_00486B53]
  bb_00486B5C[BB_00486B5C]
  bb_00486B61[BB_00486B61]
  bb_00486B66[BB_00486B66]
  bb_00486B3C -->|flow| bb_00486B47
  bb_00486B47 -->|branch| bb_00486B47
  bb_00486B47 -->|fallthrough| bb_00486B53
  bb_00486B53 -->|branch| bb_00486B61
  bb_00486B53 -->|fallthrough| bb_00486B5C
  bb_00486B5C -->|flow| bb_00486B61
```
