# KiRemoveCurrentThreadSharedReadyQueueEnumerator

- RVA: `0x002015B8`–`0x002015DB` (길이 `35` bytes)
- VA: `0x00000001402015B8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002015D0` → [KiRemoveThreadFromSharedReadyQueue](KiRemoveThreadFromSharedReadyQueue_function_002019B0.md) (function, `0x002019B0`)

### Direct callers
- [KiSearchForNewThreadsOnTarget](../30/KiSearchForNewThreadsOnTarget_function_0030F500.md) at `0x00310FE2`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002015B8  48 83 EC 28                     sub rsp, 0x28
002015BC  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
002015C0  4C 8B 40 08                     mov r8, qword ptr [rax + 8]
002015C4  4C 89 41 10                     mov qword ptr [rcx + 0x10], r8
002015C8  44 0F B6 41 0C                  movzx r8d, byte ptr [rcx + 0xc]
002015CD  48 8B 09                        mov rcx, qword ptr [rcx]
002015D0  E8 DB 03 00 00                  call 0x1402019b0
002015D5  48 83 C4 28                     add rsp, 0x28
002015D9  C3                              ret
002015DA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiRemoveCurrentThreadSharedReadyQueueEnumerator(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    *(unsigned __int64 *)(a1 + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8);
    result = KiRemoveThreadFromSharedReadyQueue(*(unsigned __int64 *)(a1), a2, *(unsigned __int8 *)(a1 + 12), a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiRemoveCurrentThreadSharedReadyQueueEnumerator(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    *(uint64_t *)(arg1 + 0x10) = *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8);
    result = KiRemoveThreadFromSharedReadyQueue(*(uint64_t *)(arg1), a2, *(uint8_t *)(arg1 + 0xC), a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0xC` | `8` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002015B8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002015B8[BB_002015B8]
  bb_002015DA[BB_002015DA]
```
