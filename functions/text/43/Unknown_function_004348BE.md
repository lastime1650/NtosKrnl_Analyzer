# sub_004348BE

- RVA: `0x004348BE`–`0x004348CE` (길이 `16` bytes)
- VA: `0x00000001404348BE`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A2A48`
- 디코드: `5`개 명령, `16/16` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004348C7` → [KiAcquirePrcbLocksForPreemptionAttemptSlowPath](KiAcquirePrcbLocksForPreemptionAttemptSlowPath_function_00434910.md) (function, `0x00434910`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x004348CC` → [sub_00434855](Unknown_function_00434855.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
004348BE  4D 8B C4                        mov r8, r12
004348C1  41 8B D1                        mov edx, r9d
004348C4  49 8B CD                        mov rcx, r13
004348C7  E8 44 00 00 00                  call 0x140434910
004348CC  EB 87                           jmp 0x140434855
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_004348BE(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;

    result = KiAcquirePrcbLocksForPreemptionAttemptSlowPath(v_r13, (unsigned int)(a4), v_r12, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_004348BE(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;

    result = KiAcquirePrcbLocksForPreemptionAttemptSlowPath(local_r13, (uint32_t)(Arg4), local_r12, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004348BE&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004348BE[BB_004348BE]
```
