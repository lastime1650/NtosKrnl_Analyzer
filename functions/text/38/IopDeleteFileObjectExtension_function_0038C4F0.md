# IopDeleteFileObjectExtension

- RVA: `0x0038C4F0`–`0x0038C51A` (길이 `42` bytes)
- VA: `0x000000014038C4F0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00080294`
- 디코드: `15`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_00863F57](../../page/86/Unknown_function_00863F57.md) at `0x00864025`
- [IopParseDevice](../../page/89/IopParseDevice_function_0089E510.md) at `0x0089FA03`
- [IopParseDevice](../../page/89/IopParseDevice_function_0089E510.md) at `0x008A044E`
- [IopParseDevice](../../page/89/IopParseDevice_function_0089E510.md) at `0x008A0624`
- [IopParseDevice](../../page/89/IopParseDevice_function_0089E510.md) at `0x008A067C`

### Static image references
- `0x0038C50E` → RVA `0x00014730` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0038C4F0  40 55                           push rbp
0038C4F2  56                              push rsi
0038C4F3  48 83 EC 48                     sub rsp, 0x48
0038C4F7  48 8B B1 D0 00 00 00            mov rsi, qword ptr [rcx + 0xd0]
0038C4FE  48 8B E9                        mov rbp, rcx
0038C501  48 85 F6                        test rsi, rsi
0038C504  75 08                           jne 0x14038c50e
0038C506  48 83 C4 48                     add rsp, 0x48
0038C50A  5E                              pop rsi
0038C50B  5D                              pop rbp
0038C50C  C3                              ret
0038C50D  CC                              int3
0038C50E  48 8D 05 1B 82 C8 FF            lea rax, [rip - 0x377de5]
0038C515  48 3B F0                        cmp rsi, rax
0038C518  74 EC                           je 0x14038c506
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopDeleteFileObjectExtension(__int64 a1)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (72);
    if (*(unsigned __int64 *)(a1 + 208) != 0) goto loc_0038C50E;
loc_0038C506:
    v_rsp = (v_rsp) + (72);
    return result;
loc_0038C50E:
    if ((*(unsigned __int64 *)(a1 + 208)) == (v_rip - 3636709)) goto loc_0038C506;
}
```

## 5. (Beta) C Style

```c
int64_t IopDeleteFileObjectExtension(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;

    local_rsp = (local_rsp) - (72);
    if (*(uint64_t *)(arg1 + 0xD0) != 0) goto loc_0038C50E;
loc_0038C506:
    local_rsp = (local_rsp) + (72);
    return result;
loc_0038C50E:
    if ((*(uint64_t *)(arg1 + 0xD0)) == (v_rip - 3636709)) goto loc_0038C506;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xD0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0038C4F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0038C4F0[BB_0038C4F0]
  bb_0038C506[BB_0038C506]
  bb_0038C50D[BB_0038C50D]
  bb_0038C50E[BB_0038C50E]
  bb_0038C4F0 -->|branch| bb_0038C50E
  bb_0038C4F0 -->|fallthrough| bb_0038C506
  bb_0038C50D -->|flow| bb_0038C50E
  bb_0038C50E -->|branch| bb_0038C506
```
