# sub_0085EA74

- RVA: `0x0085EA74`–`0x0085EA9E` (길이 `42` bytes)
- VA: `0x000000014085EA74`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006B1E0`
- 디코드: `9`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0085EA94` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (function, `0x00BC9A1C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0085EA94` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (`PAGE` → `PAGECMRC`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x0085EA7F` → [sub_0085EABD](Unknown_function_0085EABD.md) (`tail-transfer`)
  - `0x0085EA8C` → [sub_0085EABD](Unknown_function_0085EABD.md) (`tail-transfer`)
  - `0x0085EA99` → [sub_0085E7B7 + 0x32](Unknown_function_0085E7B7.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0085EA74  41 0F B7 8F BA 00 00 00         movzx ecx, word ptr [r15 + 0xba]
0085EA7C  F6 C1 04                        test cl, 4
0085EA7F  74 3C                           je 0x14085eabd
0085EA81  41 F7 85 B8 00 00 00 00 00 02 00  test dword ptr [r13 + 0xb8], 0x20000
0085EA8C  74 2F                           je 0x14085eabd
0085EA8E  49 8B CD                        mov rcx, r13
0085EA91  49 8B FF                        mov rdi, r15
0085EA94  E8 83 AF 36 00                  call 0x140bc9a1c
0085EA99  E9 4B FD FF FF                  jmp 0x14085e7e9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0085EA74(void)
{
    __int64 result;

    result = CmpLockKcbShared(v_r13, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_0085EA74(void)
{
    int64_t result;

    result = CmpLockKcbShared(local_r13, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0085EA74&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0085EA74[BB_0085EA74]
  bb_0085EA81[BB_0085EA81]
  bb_0085EA8E[BB_0085EA8E]
  bb_0085EA74 -->|fallthrough| bb_0085EA81
  bb_0085EA81 -->|fallthrough| bb_0085EA8E
```
