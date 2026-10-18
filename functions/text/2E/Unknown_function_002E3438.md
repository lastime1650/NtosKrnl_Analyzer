# sub_002E3438

- RVA: `0x002E3438`–`0x002E3459` (길이 `33` bytes)
- VA: `0x00000001402E3438`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00070E3C`
- 디코드: `7`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x002E344F` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x002E3438` → RVA `0x00F0DE58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x002E3440` → [sub_002E3191 + 0xAC](Unknown_function_002E3191.md) (`tail-transfer`)
  - `0x002E3454` → [sub_002E3191 + 0xB0](Unknown_function_002E3191.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002E3438  8B 05 1A AA C2 00               mov eax, dword ptr [rip + 0xc2aa1a]
002E343E  85 C0                           test eax, eax
002E3440  0F 85 F7 FD FF FF               jne 0x1402e323d
002E3446  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
002E344B  48 8D 4F 40                     lea rcx, [rdi + 0x40]
002E344F  E8 F0 DA FD FF                  call 0x1402c0f44
002E3454  E9 E8 FD FF FF                  jmp 0x1402e3241
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002E3438(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11)
{
    __int64 result;

    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(v_rdi + 64, a11, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_002E3438(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, int64_t Arg11)
{
    int64_t result;

    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(local_rdi + 64, Arg11, Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002E3438&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002E3438[BB_002E3438]
  bb_002E3446[BB_002E3446]
  bb_002E3438 -->|fallthrough| bb_002E3446
```
