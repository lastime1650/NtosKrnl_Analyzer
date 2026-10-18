# sub_00322F5E

- RVA: `0x00322F5E`–`0x00322F81` (길이 `35` bytes)
- VA: `0x0000000140322F5E`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000758D0`
- 디코드: `9`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00322F70` → [MiCreatePteCopyList](../48/MiCreatePteCopyList_function_004887E8.md) (function, `0x004887E8`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00322F64` → [sub_00322EC8](Unknown_function_00322EC8.md) (`tail-transfer`)
  - `0x00322F79` → [sub_00322EC8](Unknown_function_00322EC8.md) (`tail-transfer`)
  - `0x00322F7F` → [sub_00322F44](Unknown_function_00322F44.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00322F5E  44 0F 20 C0                     mov rax, cr8
00322F62  3C 02                           cmp al, 2
00322F64  0F 83 5E FF FF FF               jae 0x140322ec8
00322F6A  48 8B D3                        mov rdx, rbx
00322F6D  48 8B CE                        mov rcx, rsi
00322F70  E8 73 58 16 00                  call 0x1404887e8
00322F75  83 7B 04 00                     cmp dword ptr [rbx + 4], 0
00322F79  0F 84 49 FF FF FF               je 0x140322ec8
00322F7F  EB C3                           jmp 0x140322f44
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00322F5E(void)
{
    __int64 result;

    result = MiCreatePteCopyList(v_rsi, v_rbx, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00322F5E(void)
{
    int64_t result;

    result = MiCreatePteCopyList(local_rsi, local_rbx, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00322F5E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00322F5E[BB_00322F5E]
  bb_00322F6A[BB_00322F6A]
  bb_00322F7F[BB_00322F7F]
  bb_00322F5E -->|fallthrough| bb_00322F6A
  bb_00322F6A -->|fallthrough| bb_00322F7F
```
