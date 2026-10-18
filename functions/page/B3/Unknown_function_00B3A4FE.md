# sub_00B3A4FE

- RVA: `0x00B3A4FE`–`0x00B3A517` (길이 `25` bytes)
- VA: `0x0000000140B3A4FE`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AE5CC`
- 디코드: `7`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B3A50B` → [ZwTranslateFilePath](../../text/6B/ZwTranslateFilePath_function_006B0BD0.md) (function, `0x006B0BD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B3A50B` → [ZwTranslateFilePath](../../text/6B/ZwTranslateFilePath_function_006B0BD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B3A512` → [BiTranslateFilePath + 0x6D](../A3/BiTranslateFilePath_function_00A3D534.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B3A4FE  4C 8D 4C 24 68                  lea r9, [rsp + 0x68]
00B3A503  4C 8B C0                        mov r8, rax
00B3A506  8B D6                           mov edx, esi
00B3A508  48 8B CD                        mov rcx, rbp
00B3A50B  E8 C0 66 B7 FF                  call 0x1406b0bd0
00B3A510  8B D8                           mov ebx, eax
00B3A512  E9 8A 30 F0 FF                  jmp 0x140a3d5a1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B3A4FE(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13)
{
    __int64 result;

    result = ZwTranslateFilePath(v_rbp, (unsigned int)((unsigned int)(v_rsi)), result, a13);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B3A4FE(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, int64_t Arg13)
{
    int64_t result;

    result = ZwTranslateFilePath(local_rbp, (uint32_t)((uint32_t)(local_rsi)), result, Arg13);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B3A4FE&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B3A4FE[BB_00B3A4FE]
```
