# sub_002348B0

- RVA: `0x002348B0`–`0x002348D3` (길이 `35` bytes)
- VA: `0x00000001402348B0`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000605BC`
- 디코드: `6`개 명령, `35/35` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x002348C7` → [sub_00234B46](Unknown_function_00234B46.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002348B0  4C 89 A4 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], r12
002348B8  4C 8D A0 00 41 00 00            lea r12, [rax + 0x4100]
002348BF  4C 89 64 24 48                  mov qword ptr [rsp + 0x48], r12
002348C4  4D 85 E4                        test r12, r12
002348C7  0F 84 79 02 00 00               je 0x140234b46
002348CD  8B 89 40 94 00 00               mov ecx, dword ptr [rcx + 0x9440]
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_002348B0(__int64 a1)
{
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_pF0;

    v_stack_pF0 = v_r12;
    v_stack_p48 = result + 16640;
    return;
}
```

## 5. (Beta) C Style

```c
void sub_002348B0(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    uint64_t v_stack_p48;
    uint64_t v_stack_pF0;

    v_stack_pF0 = local_r12;
    v_stack_p48 = result + 16640;
    return;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x9440` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002348B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002348B0[BB_002348B0]
  bb_002348CD[BB_002348CD]
  bb_002348B0 -->|fallthrough| bb_002348CD
```
