# sub_002072AC

- RVA: `0x002072AC`–`0x002072CB` (길이 `31` bytes)
- VA: `0x00000001402072AC`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D150`
- 디코드: `7`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x002072C1` → [KiReleaseSpinLockInstrumented](../39/KiReleaseSpinLockInstrumented_function_00392EF0.md) (function, `0x00392EF0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x002072AC` → RVA `0x00F0DE58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x002072B4` → [sub_00207241](Unknown_function_00207241.md) (`tail-transfer`)
  - `0x002072C6` → [sub_00207241 + 0x5](Unknown_function_00207241.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002072AC  8B 05 A6 6B D0 00               mov eax, dword ptr [rip + 0xd06ba6]
002072B2  85 C0                           test eax, eax
002072B4  75 8B                           jne 0x140207241
002072B6  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
002072BE  48 8B CB                        mov rcx, rbx
002072C1  E8 2A BC 18 00                  call 0x140392ef0
002072C6  E9 7B FF FF FF                  jmp 0x140207246
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002072AC(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17)
{
    __int64 result;

    result = KiReleaseSpinLockInstrumented(v_rbx, a17, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_002072AC(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, int64_t Arg17)
{
    int64_t result;

    result = KiReleaseSpinLockInstrumented(local_rbx, Arg17, Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002072AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002072AC[BB_002072AC]
  bb_002072B6[BB_002072B6]
  bb_002072AC -->|fallthrough| bb_002072B6
```
