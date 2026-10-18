# KiUpdateGroupSchedulingRank

- RVA: `0x00355F50`–`0x00355F76` (길이 `38` bytes)
- VA: `0x0000000140355F50`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00079338`
- 디코드: `12`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KiSwapThread](KiSwapThread_function_00355640.md) at `0x00355702`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00355F70` → [sub_00356063](Unknown_function_00356063.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00355F50  44 88 4C 24 20                  mov byte ptr [rsp + 0x20], r9b
00355F55  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
00355F5A  55                              push rbp
00355F5B  56                              push rsi
00355F5C  57                              push rdi
00355F5D  41 57                           push r15
00355F5F  48 83 EC 38                     sub rsp, 0x38
00355F63  48 8B 79 68                     mov rdi, qword ptr [rcx + 0x68]
00355F67  48 8B EA                        mov rbp, rdx
00355F6A  48 8B F1                        mov rsi, rcx
00355F6D  48 85 FF                        test rdi, rdi
00355F70  0F 84 ED 00 00 00               je 0x140356063
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall KiUpdateGroupSchedulingRank(__int64 a1, __int64 a2, __int64 a3, unsigned __int8 a4)
{
    __int64 v_rsp;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p20;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_rsp = (v_rsp) - (56);
}
```

## 5. (Beta) C Style

```c
void KiUpdateGroupSchedulingRank(void *Arg1, int64_t Arg2, int64_t Arg3, uint8_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;
    uint64_t v_stack_p18;
    uint8_t v_stack_p20;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    local_rsp = (local_rsp) - (56);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x68` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00355F50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00355F50[BB_00355F50]
```
