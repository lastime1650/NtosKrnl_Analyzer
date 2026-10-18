# sub_009D5792

- RVA: `0x009D5792`–`0x009D57B2` (길이 `32` bytes)
- VA: `0x00000001409D5792`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A1DA8`
- 디코드: `7`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009D57A8` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x009D57A8` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x009D57A0` → [sub_009D56E8](Unknown_function_009D56E8.md) (`tail-transfer`)
  - `0x009D57AD` → [sub_009D56E8 + 0xF](Unknown_function_009D56E8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009D5792  4C 89 02                        mov qword ptr [rdx], r8
009D5795  49 89 50 08                     mov qword ptr [r8 + 8], rdx
009D5799  C7 43 78 00 00 00 00            mov dword ptr [rbx + 0x78], 0
009D57A0  E9 43 FF FF FF                  jmp 0x1409d56e8
009D57A5  48 8B CE                        mov rcx, rsi
009D57A8  E8 23 06 89 FF                  call 0x140265dd0
009D57AD  E9 45 FF FF FF                  jmp 0x1409d56f7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_009D5792(__int64 a1, __int64 a2, __int64 a3)
{
    *(unsigned __int64 *)(a2) = a3;
    *(unsigned __int64 *)(a3 + 8) = a2;
    *(unsigned int *)(v_rbx + 120) = 0;
}
```

## 5. (Beta) C Style

```c
int64_t sub_009D5792(int64_t Arg1, void *Arg2, void *Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;

    *(void **)(arg2) = Arg3;
    *(void **)(arg3 + 0x8) = Arg2;
    *(uint32_t *)(local_rbx + 0x78) = 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg3` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009D5792&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009D5792[BB_009D5792]
  bb_009D57A5[BB_009D57A5]
```
