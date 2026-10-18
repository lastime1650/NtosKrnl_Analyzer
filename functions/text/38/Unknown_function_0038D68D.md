# sub_0038D68D

- RVA: `0x0038D68D`–`0x0038D6B0` (길이 `35` bytes)
- VA: `0x000000014038D68D`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000804C4`
- 디코드: `7`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0038D6A6` → [KiReleaseSpinLockInstrumented](../39/KiReleaseSpinLockInstrumented_function_00392EF0.md) (function, `0x00392EF0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0038D68D` → RVA `0x00F0DE58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0038D695` → [sub_0038D2A1 + 0x289](Unknown_function_0038D2A1.md) (`tail-transfer`)
  - `0x0038D6AB` → [sub_0038D2A1 + 0x28F](Unknown_function_0038D2A1.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0038D68D  8B 05 C5 07 B8 00               mov eax, dword ptr [rip + 0xb807c5]
0038D693  85 C0                           test eax, eax
0038D695  0F 85 8F FE FF FF               jne 0x14038d52a
0038D69B  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
0038D6A3  49 8B CD                        mov rcx, r13
0038D6A6  E8 45 58 00 00                  call 0x140392ef0
0038D6AB  E9 80 FE FF FF                  jmp 0x14038d530
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0038D68D(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17)
{
    __int64 result;

    result = KiReleaseSpinLockInstrumented(v_r13, a17, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_0038D68D(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, int64_t Arg17)
{
    int64_t result;

    result = KiReleaseSpinLockInstrumented(local_r13, Arg17, Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0038D68D&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0038D68D[BB_0038D68D]
  bb_0038D69B[BB_0038D69B]
  bb_0038D68D -->|fallthrough| bb_0038D69B
```
