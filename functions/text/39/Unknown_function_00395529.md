# sub_00395529

- RVA: `0x00395529`–`0x00395550` (길이 `39` bytes)
- VA: `0x0000000140395529`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000811A8`
- 디코드: `7`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00395546` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00395529` → RVA `0x00F0DE58` (`.data`; read)
- `0x0039553F` → RVA `0x00F06590` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00395531` → [sub_003951B9 + 0x14](Unknown_function_003951B9.md) (`tail-transfer`)
  - `0x0039554B` → [sub_003951B9 + 0x1B](Unknown_function_003951B9.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00395529  8B 05 29 89 B7 00               mov eax, dword ptr [rip + 0xb78929]
0039552F  85 C0                           test eax, eax
00395531  0F 85 96 FC FF FF               jne 0x1403951cd
00395537  48 8B 94 24 B8 00 00 00         mov rdx, qword ptr [rsp + 0xb8]
0039553F  48 8D 0D 4A 10 B7 00            lea rcx, [rip + 0xb7104a]
00395546  E8 F9 B9 F2 FF                  call 0x1402c0f44
0039554B  E9 84 FC FF FF                  jmp 0x1403951d4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00395529(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23)
{
    __int64 result;

    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_rip + 11997258, a23, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00395529(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, int64_t Arg23)
{
    int64_t result;

    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_rip + 11997258, Arg23, Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00395529&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00395529[BB_00395529]
  bb_00395537[BB_00395537]
  bb_00395529 -->|fallthrough| bb_00395537
```
