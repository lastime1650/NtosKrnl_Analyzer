# sub_0024967C

- RVA: `0x0024967C`–`0x0024969C` (길이 `32` bytes)
- VA: `0x000000014024967C`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000628B4`
- 디코드: `7`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00249692` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0024967C` → RVA `0x00F0DE58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00249684` → [sub_00249517 + 0x15](Unknown_function_00249517.md) (`tail-transfer`)
  - `0x00249697` → [sub_00249517 + 0x1C](Unknown_function_00249517.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0024967C  8B 05 D6 47 CC 00               mov eax, dword ptr [rip + 0xcc47d6]
00249682  85 C0                           test eax, eax
00249684  0F 85 A2 FE FF FF               jne 0x14024952c
0024968A  48 8B 54 24 48                  mov rdx, qword ptr [rsp + 0x48]
0024968F  49 8B CE                        mov rcx, r14
00249692  E8 AD 78 07 00                  call 0x1402c0f44
00249697  E9 97 FE FF FF                  jmp 0x140249533
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0024967C(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 result;

    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_r14, a9, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_0024967C(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, int64_t Arg9)
{
    int64_t result;

    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(local_r14, Arg9, Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0024967C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0024967C[BB_0024967C]
  bb_0024968A[BB_0024968A]
  bb_0024967C -->|fallthrough| bb_0024968A
```
