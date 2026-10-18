# sub_00400A9B

- RVA: `0x00400A9B`–`0x00400ABB` (길이 `32` bytes)
- VA: `0x0000000140400A9B`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009A2C0`
- 디코드: `8`개 명령, `32/32` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x00400A9F` → [sub_00400840 + 0x124](Unknown_function_00400840.md) (`tail-transfer`)
  - `0x00400AAB` → [sub_00400840 + 0x1FB](Unknown_function_00400840.md) (`tail-transfer`)
  - `0x00400AB2` → [sub_00400840 + 0x1FE](Unknown_function_00400840.md) (`tail-transfer`)
  - `0x00400AB9` → [sub_00400840 + 0x1FE](Unknown_function_00400840.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00400A9B  48 8B 77 18                     mov rsi, qword ptr [rdi + 0x18]
00400A9F  E9 C0 FE FF FF                  jmp 0x140400964
00400AA4  81 63 04 1E 00 02 00            and dword ptr [rbx + 4], 0x2001e
00400AAB  EB 8E                           jmp 0x140400a3b
00400AAD  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00400AB2  EB 8A                           jmp 0x140400a3e
00400AB4  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00400AB9  EB 83                           jmp 0x140400a3e
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00400A9B(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_00400A9B(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00400A9B&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00400A9B[BB_00400A9B]
  bb_00400AA4[BB_00400AA4]
  bb_00400AAD[BB_00400AAD]
  bb_00400AB4[BB_00400AB4]
```
