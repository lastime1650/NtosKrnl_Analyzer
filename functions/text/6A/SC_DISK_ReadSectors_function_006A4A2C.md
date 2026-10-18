# SC_DISK::ReadSectors

- RVA: `0x006A4A2C`–`0x006A4A68` (길이 `60` bytes)
- VA: `0x00000001406A4A2C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `18`개 명령, `60/60` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006A4A5D` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [SC_GPT::ReadEntries](SC_GPT_ReadEntries_function_006A3360.md) at `0x006A33A7`
- [SC_GPT::ReadHeader](SC_GPT_ReadHeader_function_006A33E8.md) at `0x006A342B`
- [SC_DISK::ResetPartitionCache](SC_DISK_ResetPartitionCache_function_006A4A70.md) at `0x006A4A87`
- [SC_MBR::ReadPartitionTable](SC_MBR_ReadPartitionTable_function_006A5100.md) at `0x006A537E`
- [SC_MBR::WritePartitionTable](SC_MBR_WritePartitionTable_function_006A5440.md) at `0x006A562A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006A4A2C  48 83 EC 38                     sub rsp, 0x38
006A4A30  4D 8B D8                        mov r11, r8
006A4A33  4C 8B D1                        mov r10, rcx
006A4A36  4D 85 C9                        test r9, r9
006A4A39  75 07                           jne 0x1406a4a42
006A4A3B  4C 8B 89 08 01 00 00            mov r9, qword ptr [rcx + 0x108]
006A4A42  48 8B 01                        mov rax, qword ptr [rcx]
006A4A45  8B 89 F0 00 00 00               mov ecx, dword ptr [rcx + 0xf0]
006A4A4B  D3 E2                           shl edx, cl
006A4A4D  49 D3 E3                        shl r11, cl
006A4A50  44 8B C2                        mov r8d, edx
006A4A53  48 8B 40 38                     mov rax, qword ptr [rax + 0x38]
006A4A57  49 8B D3                        mov rdx, r11
006A4A5A  49 8B CA                        mov rcx, r10
006A4A5D  E8 6E 60 01 00                  call 0x1406baad0
006A4A62  48 83 C4 38                     add rsp, 0x38
006A4A66  C3                              ret
006A4A67  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SC_DISK__ReadSectors(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (56);
    if (a4 == 0) {
        a4 = *(unsigned __int64 *)(a1 + 264);
    }
    a2 = (unsigned int)((a2) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 240)))));
    v_r11 = (a3) << ((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 240))));
    result = guard_dispatch_icall(a1, v_r11, (unsigned int)(a2), a4);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SC_DISK__ReadSectors(void *Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r11;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (56);
    if (Arg4 == 0) {
        Arg4 = *(uint64_t *)(arg1 + 0x108);
    }
    Arg2 = (uint32_t)((Arg2) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xF0)))));
    local_r11 = (Arg3) << ((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xF0))));
    result = guard_dispatch_icall(Arg1, local_r11, (uint32_t)(Arg2), Arg4);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0xF0` | `32` | `R` |
| `Arg1` | `+ 0x108` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006A4A2C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006A4A2C[BB_006A4A2C]
  bb_006A4A3B[BB_006A4A3B]
  bb_006A4A42[BB_006A4A42]
  bb_006A4A67[BB_006A4A67]
  bb_006A4A2C -->|branch| bb_006A4A42
  bb_006A4A2C -->|fallthrough| bb_006A4A3B
  bb_006A4A3B -->|flow| bb_006A4A42
```
