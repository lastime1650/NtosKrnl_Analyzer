# PspFindVsmEnclaveThread

- RVA: `0x00A0D5F0`–`0x00A0D608` (길이 `24` bytes)
- VA: `0x0000000140A0D5F0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PsAdjustBasicEnclaveThreadList](../../text/5E/PsAdjustBasicEnclaveThreadList_function_005E4BD8.md) at `0x005E4C90`
- [PsAdjustBasicEnclaveThreadList](../../text/5E/PsAdjustBasicEnclaveThreadList_function_005E4BD8.md) at `0x005E4CC7`
- [PsLoadVsmEnclaveData](../../text/5E/PsLoadVsmEnclaveData_function_005E4D5C.md) at `0x005E4E59`
- [PsCallEnclave](PsCallEnclave_function_00A0CF50.md) at `0x00A0D103`
- [PsCallEnclave](PsCallEnclave_function_00A0CF50.md) at `0x00A0D358`
- [sub_00B36710](../B3/Unknown_function_00B36710.md) at `0x00B3688A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A0D5F0  4C 8B 42 18                     mov r8, qword ptr [rdx + 0x18]
00A0D5F4  49 3B C8                        cmp rcx, r8
00A0D5F7  72 0A                           jb 0x140a0d603
00A0D5F9  33 C0                           xor eax, eax
00A0D5FB  49 3B C8                        cmp rcx, r8
00A0D5FE  0F 97 C0                        seta al
00A0D601  C3                              ret
00A0D602  CC                              int3
00A0D603  83 C8 FF                        or eax, 0xffffffff
00A0D606  C3                              ret
00A0D607  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspFindVsmEnclaveThread(__int64 a1, __int64 a2)
{
    __int64 result;

    if (a1 < (*(unsigned __int64 *)(a2 + 24))) goto loc_00A0D603;
    result = 0;
    result = (a1 > (*(unsigned __int64 *)(a2 + 24))) ? 1 : 0;
    return result;
loc_00A0D603:
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PspFindVsmEnclaveThread(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if (Arg1 < (*(uint64_t *)(arg2 + 0x18))) goto loc_00A0D603;
    result = 0;
    result = (Arg1 > (*(uint64_t *)(arg2 + 0x18))) ? 1 : 0;
    return result;
loc_00A0D603:
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A0D5F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A0D5F0[BB_00A0D5F0]
  bb_00A0D5F9[BB_00A0D5F9]
  bb_00A0D602[BB_00A0D602]
  bb_00A0D603[BB_00A0D603]
  bb_00A0D607[BB_00A0D607]
  bb_00A0D5F0 -->|branch| bb_00A0D603
  bb_00A0D5F0 -->|fallthrough| bb_00A0D5F9
  bb_00A0D602 -->|flow| bb_00A0D603
```
