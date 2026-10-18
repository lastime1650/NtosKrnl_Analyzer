# sub_008C76DB

- RVA: `0x008C76DB`–`0x008C76F3` (길이 `24` bytes)
- VA: `0x00000001408C76DB`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00083F00`
- 디코드: `6`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x008C76E2` → [sub_008C7637 + 0x17](Unknown_function_008C7637.md) (`tail-transfer`)
  - `0x008C76EE` → [sub_008C7637 + 0x24](Unknown_function_008C7637.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008C76DB  48 8B 4A 38                     mov rcx, qword ptr [rdx + 0x38]
008C76DF  48 85 C9                        test rcx, rcx
008C76E2  0F 84 66 FF FF FF               je 0x1408c764e
008C76E8  48 3B C1                        cmp rax, rcx
008C76EB  0F 94 C0                        sete al
008C76EE  E9 68 FF FF FF                  jmp 0x1408c765b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_008C76DB(__int64 a1, __int64 a2)
{
    __int64 result;

    result = (result == (*(unsigned __int64 *)(a2 + 56))) ? 1 : 0;
}
```

## 5. (Beta) C Style

```c
int64_t sub_008C76DB(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    result = (result == (*(uint64_t *)(arg2 + 0x38))) ? 1 : 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x38` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008C76DB&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008C76DB[BB_008C76DB]
  bb_008C76E8[BB_008C76E8]
  bb_008C76DB -->|fallthrough| bb_008C76E8
```
