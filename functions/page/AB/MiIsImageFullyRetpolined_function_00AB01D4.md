# MiIsImageFullyRetpolined

- RVA: `0x00AB01D4`–`0x00AB020F` (길이 `59` bytes)
- VA: `0x0000000140AB01D4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068784`
- 디코드: `18`개 명령, `59/59` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AB01E4` → [MiSectionControlArea](../../text/29/MiSectionControlArea_function_00294CB0.md) (function, `0x00294CB0`)
- `0x00AB0208` → [RtlIsImageFullyRetpolined](../../text/4C/RtlIsImageFullyRetpolined_function_004CDE74.md) (function, `0x004CDE74`)

### Direct callers
- [MiMarkKernelImageRetpolineBits](../AA/MiMarkKernelImageRetpolineBits_function_00AA0348.md) at `0x00AA0383`
- [MiUnloadSystemImage](../AA/MiUnloadSystemImage_function_00AA2FD4.md) at `0x00AA3161`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00AB01E4` → [MiSectionControlArea](../../text/29/MiSectionControlArea_function_00294CB0.md) (`PAGE` → `.text`)
  - `0x00AB0208` → [RtlIsImageFullyRetpolined](../../text/4C/RtlIsImageFullyRetpolined_function_004CDE74.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB01D4  48 83 EC 28                     sub rsp, 0x28
00AB01D8  48 8B 41 70                     mov rax, qword ptr [rcx + 0x70]
00AB01DC  48 85 C0                        test rax, rax
00AB01DF  74 23                           je 0x140ab0204
00AB01E1  48 8B C8                        mov rcx, rax
00AB01E4  E8 C7 4A 7E FF                  call 0x140294cb0
00AB01E9  48 8B 40 60                     mov rax, qword ptr [rax + 0x60]
00AB01ED  48 83 E0 F8                     and rax, 0xfffffffffffffff8
00AB01F1  48 8B 40 20                     mov rax, qword ptr [rax + 0x20]
00AB01F5  8B 40 48                        mov eax, dword ptr [rax + 0x48]
00AB01F8  C1 E8 05                        shr eax, 5
00AB01FB  83 E0 01                        and eax, 1
00AB01FE  48 83 C4 28                     add rsp, 0x28
00AB0202  C3                              ret
00AB0203  CC                              int3
00AB0204  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
00AB0208  E8 67 DC A1 FF                  call 0x1404cde74
00AB020D  EB EF                           jmp 0x140ab01fe
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiIsImageFullyRetpolined(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(a1 + 112) == 0) goto loc_00AB0204;
    result = MiSectionControlArea(*(unsigned __int64 *)(a1 + 112), a2, a3, a4);
    result = (*(unsigned __int64 *)(result + 96)) & (-8);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 72))) >> (5));
    result = (unsigned int)((result) & (1));
loc_00AB01FE:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00AB0204:
    result = RtlIsImageFullyRetpolined(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 112) + 48), a2, a3, a4);
    goto loc_00AB01FE;
}
```

## 5. (Beta) C Style

```c
int64_t MiIsImageFullyRetpolined(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(arg1 + 0x70) == 0) goto loc_00AB0204;
    result = MiSectionControlArea(*(uint64_t *)(arg1 + 0x70), a2, a3, a4);
    result = (*(uint64_t *)(result + 0x60)) & (-8);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0x48))) >> (5));
    result = (uint32_t)((result) & (1));
loc_00AB01FE:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00AB0204:
    result = RtlIsImageFullyRetpolined(*(uint64_t *)(*(uint64_t *)(arg1 + 0x70) + 0x30), a2, a3, a4);
    goto loc_00AB01FE;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB01D4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AB01D4[BB_00AB01D4]
  bb_00AB01E1[BB_00AB01E1]
  bb_00AB01FE[BB_00AB01FE]
  bb_00AB0203[BB_00AB0203]
  bb_00AB0204[BB_00AB0204]
  bb_00AB01D4 -->|branch| bb_00AB0204
  bb_00AB01D4 -->|fallthrough| bb_00AB01E1
  bb_00AB01E1 -->|flow| bb_00AB01FE
  bb_00AB0203 -->|flow| bb_00AB0204
  bb_00AB0204 -->|branch| bb_00AB01FE
```
