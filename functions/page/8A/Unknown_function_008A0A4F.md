# sub_008A0A4F

- RVA: `0x008A0A4F`–`0x008A0A68` (길이 `25` bytes)
- VA: `0x00000001408A0A4F`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007E904`
- 디코드: `7`개 명령, `25/25` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x008A0A51` → [sub_008A0A82](Unknown_function_008A0A82.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008A0A4F  84 D2                           test dl, dl
008A0A51  75 2F                           jne 0x1408a0a82
008A0A53  45 84 F6                        test r14b, r14b
008A0A56  75 06                           jne 0x1408a0a5e
008A0A58  81 26 FF BF FF FF               and dword ptr [rsi], 0xffffbfff
008A0A5E  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
008A0A63  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_008A0A4F(__int64 a1, unsigned __int8 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15)
{
    if ((unsigned __int8)(v_r14) == 0) {
    }
    return;
}
```

## 5. (Beta) C Style

```c
void sub_008A0A4F(int64_t Arg1, uint8_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, int64_t Arg12, uint64_t Arg13, uint64_t Arg14, int64_t Arg15)
{
    if ((uint8_t)(local_r14) == 0) {
    }
    return;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008A0A4F&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008A0A4F[BB_008A0A4F]
  bb_008A0A53[BB_008A0A53]
  bb_008A0A58[BB_008A0A58]
  bb_008A0A5E[BB_008A0A5E]
  bb_008A0A4F -->|fallthrough| bb_008A0A53
  bb_008A0A53 -->|branch| bb_008A0A5E
  bb_008A0A53 -->|fallthrough| bb_008A0A58
  bb_008A0A58 -->|flow| bb_008A0A5E
```
