# IopParseDevice$fin$0

- RVA: `0x00B0E920`–`0x00B0E949` (길이 `41` bytes)
- VA: `0x0000000140B0E920`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007E880`
- 디코드: `13`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B0E93C` → [VfFastIoCheckState](../../pagevrfy/BB/VfFastIoCheckState_function_00BB9440.md) (function, `0x00BB9440`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B0E93C` → [VfFastIoCheckState](../../pagevrfy/BB/VfFastIoCheckState_function_00BB9440.md) (`PAGE` → `PAGEVRFY`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B0E920  40 55                           push rbp
00B0E922  48 83 EC 60                     sub rsp, 0x60
00B0E926  48 8B EA                        mov rbp, rdx
00B0E929  48 8B 8D 58 01 00 00            mov rcx, qword ptr [rbp + 0x158]
00B0E930  48 85 C9                        test rcx, rcx
00B0E933  74 0D                           je 0x140b0e942
00B0E935  48 8B 95 08 01 00 00            mov rdx, qword ptr [rbp + 0x108]
00B0E93C  E8 FF AA 0A 00                  call 0x140bb9440
00B0E941  90                              nop
00B0E942  48 83 C4 60                     add rsp, 0x60
00B0E946  5D                              pop rbp
00B0E947  C3                              ret
00B0E948  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopParseDevice_fin_0(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (96);
    if (*(unsigned __int64 *)(a2 + 344) != 0) {
        a2 = *(unsigned __int64 *)(a2 + 264);
        result = VfFastIoCheckState(*(unsigned __int64 *)(a2 + 344), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (96);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopParseDevice_fin_0(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (96);
    if (*(uint64_t *)(arg2 + 0x158) != 0) {
        Arg2 = *(uint64_t *)(arg2 + 0x108);
        result = VfFastIoCheckState(*(uint64_t *)(arg2 + 0x158), Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (96);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x108` | `64` | `R` |
| `Arg2` | `+ 0x158` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B0E920&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B0E920[BB_00B0E920]
  bb_00B0E935[BB_00B0E935]
  bb_00B0E942[BB_00B0E942]
  bb_00B0E948[BB_00B0E948]
  bb_00B0E920 -->|branch| bb_00B0E942
  bb_00B0E920 -->|fallthrough| bb_00B0E935
  bb_00B0E935 -->|flow| bb_00B0E942
```
