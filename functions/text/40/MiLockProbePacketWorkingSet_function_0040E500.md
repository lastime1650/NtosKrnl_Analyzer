# MiLockProbePacketWorkingSet

- RVA: `0x0040E500`–`0x0040E525` (길이 `37` bytes)
- VA: `0x000000014040E500`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009B8B4`
- 디코드: `10`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiProbeAndLockPacket](../23/MiProbeAndLockPacket_function_0023BE20.md) at `0x0023C0DA`
- [sub_0023D89B](../23/Unknown_function_0023D89B.md) at `0x0023D8D6`
- [sub_0023F9E7](../23/Unknown_function_0023F9E7.md) at `0x0023FA41`
- [MiFaultInProbeAddress](MiFaultInProbeAddress_function_0040E108.md) at `0x0040E1CA`
- [MiInitializeProbePacketVm](MiInitializeProbePacketVm_function_0040E240.md) at `0x0040E2E7`
- [MiInitializeProbePacketVm](MiInitializeProbePacketVm_function_0040E240.md) at `0x0040E399`
- [MiSplitReducedCommitClonePage](../4F/MiSplitReducedCommitClonePage_function_004FA808.md) at `0x004FA8A8`
- [MiSplitReducedCommitClonePage](../4F/MiSplitReducedCommitClonePage_function_004FA808.md) at `0x004FA9C3`
- [sub_006D7AEE](../6D/Unknown_function_006D7AEE.md) at `0x006D7B2C`
- [sub_006D7AEE](../6D/Unknown_function_006D7AEE.md) at `0x006D7BA5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0040E517` → [sub_0040E659](Unknown_function_0040E659.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0040E500  40 53                           push rbx
0040E502  48 83 EC 20                     sub rsp, 0x20
0040E506  83 61 48 CF                     and dword ptr [rcx + 0x48], 0xffffffcf
0040E50A  48 8B D9                        mov rbx, rcx
0040E50D  44 0F 20 C0                     mov rax, cr8
0040E511  48 8B 49 68                     mov rcx, qword ptr [rcx + 0x68]
0040E515  3C 02                           cmp al, 2
0040E517  0F 84 3C 01 00 00               je 0x14040e659
0040E51D  8B 81 B8 00 00 00               mov eax, dword ptr [rcx + 0xb8]
0040E523  24 0F                           and al, 0xf
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiLockProbePacketWorkingSet(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = (unsigned __int8)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 104) + 184))) & (15));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiLockProbePacketWorkingSet(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = (uint8_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x68) + 0xB8))) & (15));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x48` | `32` | `R/W` |
| `Arg1` | `+ 0x68` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0040E500&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0040E500[BB_0040E500]
  bb_0040E51D[BB_0040E51D]
  bb_0040E500 -->|fallthrough| bb_0040E51D
```
