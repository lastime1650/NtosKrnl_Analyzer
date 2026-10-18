# VfMiscKeReleaseQueuedSpinLock_Entry

- RVA: `0x00BADEE0`–`0x00BADEFC` (길이 `28` bytes)
- VA: `0x0000000140BADEE0`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00BADEF1` → [ViMiscCheckKeLowerIrql](../BB/ViMiscCheckKeLowerIrql_function_00BB81C4.md) (function, `0x00BB81C4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00BADEE0  48 83 EC 28                     sub rsp, 0x28
00BADEE4  48 8B D1                        mov rdx, rcx
00BADEE7  44 0F 20 C1                     mov rcx, cr8
00BADEEB  4C 8B 02                        mov r8, qword ptr [rdx]
00BADEEE  8A 52 08                        mov dl, byte ptr [rdx + 8]
00BADEF1  E8 CE A2 00 00                  call 0x140bb81c4
00BADEF6  48 83 C4 28                     add rsp, 0x28
00BADEFA  C3                              ret
00BADEFB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfMiscKeReleaseQueuedSpinLock_Entry(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ViMiscCheckKeLowerIrql(v_cr8, *(unsigned __int8 *)(a1 + 8), *(unsigned __int64 *)(a1), a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VfMiscKeReleaseQueuedSpinLock_Entry(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ViMiscCheckKeLowerIrql(v_cr8, *(uint8_t *)(arg1 + 0x8), *(uint64_t *)(arg1), a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00BADEE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00BADEE0[BB_00BADEE0]
  bb_00BADEFB[BB_00BADEFB]
```
