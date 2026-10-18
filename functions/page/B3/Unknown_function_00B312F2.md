# sub_00B312F2

- RVA: `0x00B312F2`–`0x00B3130A` (길이 `24` bytes)
- VA: `0x0000000140B312F2`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A629C`
- 디코드: `6`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B312F8` → [RtlRbRemoveNode](../../text/2E/RtlRbRemoveNode_function_002E4C10.md) (function, `0x002E4C10`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B312F8` → [RtlRbRemoveNode](../../text/2E/RtlRbRemoveNode_function_002E4C10.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B31305` → [EtwpSetProviderTraitsCommon + 0x12F](../9F/EtwpSetProviderTraitsCommon_function_009F36EC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B312F2  48 8B D7                        mov rdx, rdi
00B312F5  49 8B CC                        mov rcx, r12
00B312F8  E8 13 39 7B FF                  call 0x1402e4c10
00B312FD  4C 8B EF                        mov r13, rdi
00B31300  BB 01 00 00 C0                  mov ebx, 0xc0000001
00B31305  E9 11 25 EC FF                  jmp 0x1409f381b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B312F2(void)
{
    __int64 result;

    result = RtlRbRemoveNode(v_r12, v_rdi, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00B312F2(void)
{
    int64_t result;

    result = RtlRbRemoveNode(local_r12, local_rdi, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B312F2&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B312F2[BB_00B312F2]
```
