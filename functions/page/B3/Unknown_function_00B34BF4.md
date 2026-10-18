# sub_00B34BF4

- RVA: `0x00B34BF4`–`0x00B34C12` (길이 `30` bytes)
- VA: `0x0000000140B34BF4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A88B0`
- 디코드: `7`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B34BF8` → [PoFxIdleDevice](../../text/48/PoFxIdleDevice_function_00483EE8.md) (function, `0x00483EE8`)
- `0x00B34C07` → [PnpCancelRemoveLockedDeviceNode](../72/PnpCancelRemoveLockedDeviceNode_function_0072CFE0.md) (function, `0x0072CFE0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B34BF8` → [PoFxIdleDevice](../../text/48/PoFxIdleDevice_function_00483EE8.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B34C0D` → [PnpDeleteLockedDeviceNode + 0x36](../A0/PnpDeleteLockedDeviceNode_function_00A09DC4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B34BF4  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
00B34BF8  E8 EB F2 94 FF                  call 0x140483ee8
00B34BFD  83 A3 C0 02 00 00 FB            and dword ptr [rbx + 0x2c0], 0xfffffffb
00B34C04  48 8B CB                        mov rcx, rbx
00B34C07  E8 D4 83 BF FF                  call 0x14072cfe0
00B34C0C  90                              nop
00B34C0D  E9 E8 51 ED FF                  jmp 0x140a09dfa
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B34BF4(__int64 a1)
{
    __int64 result;

    result = PoFxIdleDevice(*(unsigned __int64 *)(a1 + 32), a2, a3, a4);
    result = PnpCancelRemoveLockedDeviceNode(v_rbx, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B34BF4(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = PoFxIdleDevice(*(uint64_t *)(arg1 + 0x20), a2, a3, a4);
    result = PnpCancelRemoveLockedDeviceNode(local_rbx, a2, a3, a4);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B34BF4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B34BF4[BB_00B34BF4]
```
