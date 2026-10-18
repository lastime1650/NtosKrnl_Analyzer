# sub_00857EB2

- RVA: `0x00857EB2`–`0x00857ED3` (길이 `33` bytes)
- VA: `0x0000000140857EB2`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006A6F0`
- 디코드: `8`개 명령, `33/33` bytes 표시
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
  - `0x00857EBA` → [CmpGetSymbolicLinkTarget + 0x475](CmpGetSymbolicLinkTarget_function_008570A0.md) (`tail-transfer`)
  - `0x00857ECE` → [CmpGetSymbolicLinkTarget + 0x5DD](CmpGetSymbolicLinkTarget_function_008570A0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00857EB2  BF 34 00 00 C0                  mov edi, 0xc0000034
00857EB7  41 B6 01                        mov r14b, 1
00857EBA  E9 56 F6 FF FF                  jmp 0x140857515
00857EBF  81 FF 34 00 00 C0               cmp edi, 0xc0000034
00857EC5  75 F0                           jne 0x140857eb7
00857EC7  4C 8B 45 E0                     mov r8, qword ptr [rbp - 0x20]
00857ECB  66 FF CE                        dec si
00857ECE  E9 AA F7 FF FF                  jmp 0x14085767d
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00857EB2(void)
{
loc_00857EB7:
}
```

## 5. (Beta) C Style

```c
void sub_00857EB2(void)
{
loc_00857EB7:
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00857EB2&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00857EB2[BB_00857EB2]
  bb_00857EB7[BB_00857EB7]
  bb_00857EBF[BB_00857EBF]
  bb_00857EC7[BB_00857EC7]
  bb_00857EB2 -->|flow| bb_00857EB7
  bb_00857EBF -->|branch| bb_00857EB7
  bb_00857EBF -->|fallthrough| bb_00857EC7
```
