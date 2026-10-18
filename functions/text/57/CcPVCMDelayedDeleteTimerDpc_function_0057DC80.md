# CcPVCMDelayedDeleteTimerDpc

- RVA: `0x0057DC80`–`0x0057DCA0` (길이 `32` bytes)
- VA: `0x000000014057DC80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0057DC95` → [ExQueueWorkItemToPartition](../35/ExQueueWorkItemToPartition_function_00356E2C.md) (function, `0x00356E2C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0057DC80  48 83 EC 28                     sub rsp, 0x28
0057DC84  4C 8B 4A 08                     mov r9, qword ptr [rdx + 8]
0057DC88  48 8D 8A E8 05 00 00            lea rcx, [rdx + 0x5e8]
0057DC8F  33 D2                           xor edx, edx
0057DC91  41 83 C8 FF                     or r8d, 0xffffffff
0057DC95  E8 92 91 DD FF                  call 0x140356e2c
0057DC9A  48 83 C4 28                     add rsp, 0x28
0057DC9E  C3                              ret
0057DC9F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CcPVCMDelayedDeleteTimerDpc(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = 0;
    a3 = (unsigned int)((a3) | (0xFFFFFFFFULL));
    result = ExQueueWorkItemToPartition(a2 + 1512, a2, a3, *(unsigned __int64 *)(a2 + 8));
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CcPVCMDelayedDeleteTimerDpc(int64_t Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = 0;
    Arg3 = (uint32_t)((Arg3) | (0xFFFFFFFFULL));
    result = ExQueueWorkItemToPartition(Arg2 + 1512, Arg2, Arg3, *(uint64_t *)(arg2 + 0x8));
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x5E8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0057DC80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0057DC80[BB_0057DC80]
  bb_0057DC9F[BB_0057DC9F]
```
