# sub_00B1A8E2

- RVA: `0x00B1A8E2`–`0x00B1A8FB` (길이 `25` bytes)
- VA: `0x0000000140B1A8E2`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082BFC`
- 디코드: `7`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B1A8F0` → [PspWriteTebImpersonationInfo](../8C/PspWriteTebImpersonationInfo_function_008CC7F0.md) (function, `0x008CC7F0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00B1A8E4` → [NtOpenThreadTokenEx + 0x516](../8B/NtOpenThreadTokenEx_function_008B7840.md) (`tail-transfer`)
  - `0x00B1A8F6` → [NtOpenThreadTokenEx + 0x516](../8B/NtOpenThreadTokenEx_function_008B7840.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B1A8E2  84 DB                           test bl, bl
00B1A8E4  0F 84 6C D4 D9 FF               je 0x1408b7d56
00B1A8EA  48 8B D7                        mov rdx, rdi
00B1A8ED  49 8B CE                        mov rcx, r14
00B1A8F0  E8 FB 1E DB FF                  call 0x1408cc7f0
00B1A8F5  90                              nop
00B1A8F6  E9 5B D4 D9 FF                  jmp 0x1408b7d56
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B1A8E2(void)
{
    __int64 result;

    result = PspWriteTebImpersonationInfo(v_r14, v_rdi, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00B1A8E2(void)
{
    int64_t result;

    result = PspWriteTebImpersonationInfo(local_r14, local_rdi, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B1A8E2&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B1A8E2[BB_00B1A8E2]
  bb_00B1A8EA[BB_00B1A8EA]
  bb_00B1A8E2 -->|fallthrough| bb_00B1A8EA
```
