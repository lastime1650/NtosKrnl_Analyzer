# FsRtlNotifyReportChange

- RVA: `0x00716E90`–`0x00716ED0` (길이 `64` bytes)
- VA: `0x0000000140716E90`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CC98`
- 디코드: `17`개 명령, `64/64` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00716EC5` → [FsRtlNotifyFilterReportChange](../A1/FsRtlNotifyFilterReportChange_function_00A1E880.md) (function, `0x00A1E880`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00716E90  4C 8B DC                        mov r11, rsp
00716E93  48 83 EC 58                     sub rsp, 0x58
00716E97  41 0F B7 01                     movzx eax, word ptr [r9]
00716E9B  45 33 D2                        xor r10d, r10d
00716E9E  45 0F B7 08                     movzx r9d, word ptr [r8]
00716EA2  4D 89 53 F0                     mov qword ptr [r11 - 0x10], r10
00716EA6  66 44 2B C8                     sub r9w, ax
00716EAA  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
00716EB1  4D 89 53 E8                     mov qword ptr [r11 - 0x18], r10
00716EB5  45 89 53 E0                     mov dword ptr [r11 - 0x20], r10d
00716EB9  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00716EBD  4D 89 53 D0                     mov qword ptr [r11 - 0x30], r10
00716EC1  4D 89 53 C8                     mov qword ptr [r11 - 0x38], r10
00716EC5  E8 B6 79 30 00                  call 0x140a1e880
00716ECA  48 83 C4 58                     add rsp, 0x58
00716ECE  C3                              ret
00716ECF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlNotifyReportChange(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (88);
    v_r10 = 0;
    *(unsigned __int64 *)(v_rsp - 16) = 0;
    a4 = (unsigned __int16)((*(unsigned __int16 *)(a3)) - ((unsigned __int16)(*(unsigned __int16 *)(a4))));
    *(unsigned __int64 *)(v_rsp - 24) = 0;
    *(unsigned int *)(v_rsp - 32) = 0;
    v_stack_m28 = (unsigned int)((unsigned int)(a5));
    *(unsigned __int64 *)(v_rsp - 48) = 0;
    *(unsigned __int64 *)(v_rsp - 56) = 0;
    result = FsRtlNotifyFilterReportChange(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlNotifyReportChange(int64_t Arg1, int64_t Arg2, void *Arg3, void *Arg4, uint32_t Arg5)
{
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (88);
    local_r10 = 0;
    *(uint64_t *)(local_rsp - 0x10) = 0;
    Arg4 = (uint16_t)((*(uint16_t *)(arg3)) - ((uint16_t)(*(uint16_t *)(arg4))));
    *(uint64_t *)(local_rsp - 0x18) = 0;
    *(uint32_t *)(local_rsp - 0x20) = 0;
    v_stack_m28 = (uint32_t)((uint32_t)(Arg5));
    *(uint64_t *)(local_rsp - 0x30) = 0;
    *(uint64_t *)(local_rsp - 0x38) = 0;
    result = FsRtlNotifyFilterReportChange(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (88);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `16` | `R` |
| `Arg4` | `+ 0x0` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00716E90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00716E90[BB_00716E90]
  bb_00716ECF[BB_00716ECF]
```
