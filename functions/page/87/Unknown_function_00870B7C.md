# sub_00870B7C

- RVA: `0x00870B7C`–`0x00870B96` (길이 `26` bytes)
- VA: `0x0000000140870B7C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006C320`
- 디코드: `8`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00870B8F` → [SepAuditFailed](../86/SepAuditFailed_function_0086EE20.md) (function, `0x0086EE20`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00870B7F` → [sub_00870B27 + 0x1C](Unknown_function_00870B27.md) (`tail-transfer`)
  - `0x00870B88` → [sub_00870B27 + 0x24](Unknown_function_00870B27.md) (`tail-transfer`)
  - `0x00870B94` → [sub_00870B27 + 0x42](Unknown_function_00870B27.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00870B7C  4D 8B FE                        mov r15, r14
00870B7F  EB C2                           jmp 0x140870b43
00870B81  4D 8B 4F 10                     mov r9, qword ptr [r15 + 0x10]
00870B85  4D 85 C9                        test r9, r9
00870B88  75 C1                           jne 0x140870b4b
00870B8A  B9 7C 00 00 C0                  mov ecx, 0xc000007c
00870B8F  E8 8C E2 FF FF                  call 0x14086ee20
00870B94  EB D3                           jmp 0x140870b69
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00870B7C(void)
{
}
```

## 5. (Beta) C Style

```c
void sub_00870B7C(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00870B7C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00870B7C[BB_00870B7C]
  bb_00870B81[BB_00870B81]
  bb_00870B8A[BB_00870B8A]
  bb_00870B81 -->|fallthrough| bb_00870B8A
```
