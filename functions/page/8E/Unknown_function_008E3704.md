# sub_008E3704

- RVA: `0x008E3704`–`0x008E372B` (길이 `39` bytes)
- VA: `0x00000001408E3704`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008608C`
- 디코드: `9`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x008E3712` → RVA `0x00F8B6C0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x008E3707` → [sub_008E3772 + 0x1E](Unknown_function_008E3772.md) (`tail-transfer`)
  - `0x008E3710` → [sub_008E3772 + 0xD](Unknown_function_008E3772.md) (`tail-transfer`)
  - `0x008E3719` → [sub_008E2AB2 + 0x19](Unknown_function_008E2AB2.md) (`tail-transfer`)
  - `0x008E3726` → [sub_008E28A3 + 0x158](Unknown_function_008E28A3.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008E3704  83 E9 01                        sub ecx, 1
008E3707  0F 84 83 00 00 00               je 0x1408e3790
008E370D  83 E9 02                        sub ecx, 2
008E3710  75 6D                           jne 0x1408e377f
008E3712  48 8D 35 A7 7F 6A 00            lea rsi, [rip + 0x6a7fa7]
008E3719  E9 AD F3 FF FF                  jmp 0x1408e2acb
008E371E  44 8B 5C 24 6C                  mov r11d, dword ptr [rsp + 0x6c]
008E3723  45 33 FF                        xor r15d, r15d
008E3726  E9 D0 F2 FF FF                  jmp 0x1408e29fb
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_008E3704(int a1)
{
    unsigned int v_stack_p6C;

    a1 = (unsigned int)((a1) - (1));
    a1 = (unsigned int)((a1) - (2));
}
```

## 5. (Beta) C Style

```c
void sub_008E3704(int32_t Arg1)
{
    uint32_t v_stack_p6C;

    Arg1 = (uint32_t)((Arg1) - (1));
    Arg1 = (uint32_t)((Arg1) - (2));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008E3704&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008E3704[BB_008E3704]
  bb_008E370D[BB_008E370D]
  bb_008E3712[BB_008E3712]
  bb_008E371E[BB_008E371E]
  bb_008E3704 -->|fallthrough| bb_008E370D
  bb_008E370D -->|fallthrough| bb_008E3712
```
