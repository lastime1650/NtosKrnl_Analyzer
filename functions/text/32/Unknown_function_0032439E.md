# sub_0032439E

- RVA: `0x0032439E`–`0x003243BB` (길이 `29` bytes)
- VA: `0x000000014032439E`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00075A60`
- 디코드: `6`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x003243B1` → [ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented](../2C/ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented_function_002C0F44.md) (function, `0x002C0F44`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0032439E` → RVA `0x00F0DE58` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x003243A6` → [sub_003242D8 + 0xD](Unknown_function_003242D8.md) (`tail-transfer`)
  - `0x003243B6` → [sub_003242D8 + 0x13](Unknown_function_003242D8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0032439E  8B 05 B4 9A BE 00               mov eax, dword ptr [rip + 0xbe9ab4]
003243A4  85 C0                           test eax, eax
003243A6  0F 85 39 FF FF FF               jne 0x1403242e5
003243AC  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
003243B1  E8 8E CB F9 FF                  call 0x1402c0f44
003243B6  E9 30 FF FF FF                  jmp 0x1403242eb
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0032439E(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7)
{
    __int64 result;

    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(a1, a7, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_0032439E(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, int64_t Arg7)
{
    int64_t result;

    result = ExpReleaseSpinLockExclusiveFromDpcLevelInstrumented(Arg1, Arg7, Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0032439E&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0032439E[BB_0032439E]
  bb_003243AC[BB_003243AC]
  bb_0032439E -->|fallthrough| bb_003243AC
```
