# RtlpHpLfhContextUpdateConfig

- RVA: `0x00604C3C`–`0x00604C72` (길이 `54` bytes)
- VA: `0x0000000140604C3C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `16`개 명령, `54/54` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [RtlpHpLfhContextEnable](RtlpHpLfhContextEnable_function_0060484C.md) at `0x00604879`
- [ExpPrivatePoolCreate](../../page/7D/ExpPrivatePoolCreate_function_007D5F98.md) at `0x007D612C`

### Static image references
- `0x00604C3C` → RVA `0x00F059A0` (`.data`; read)
- `0x00604C4B` → RVA `0x00E28328` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00604C3C  8B 05 5E 0D 90 00               mov eax, dword ptr [rip + 0x900d5e]
00604C42  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
00604C47  A8 04                           test al, 4
00604C49  74 0E                           je 0x140604c59
00604C4B  8B 05 D7 36 82 00               mov eax, dword ptr [rip + 0x8236d7]
00604C51  A8 04                           test al, 4
00604C53  74 04                           je 0x140604c59
00604C55  83 49 48 01                     or dword ptr [rcx + 0x48], 1
00604C59  8B 02                           mov eax, dword ptr [rdx]
00604C5B  89 44 24 18                     mov dword ptr [rsp + 0x18], eax
00604C5F  B8 F1 FF 00 00                  mov eax, 0xfff1
00604C64  66 01 44 24 18                  add word ptr [rsp + 0x18], ax
00604C69  8B 44 24 18                     mov eax, dword ptr [rsp + 0x18]
00604C6D  89 41 44                        mov dword ptr [rcx + 0x44], eax
00604C70  C3                              ret
00604C71  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpHpLfhContextUpdateConfig(__int64 a1, __int64 a2, int a3)
{
    unsigned int v_stack_p18;

    v_stack_p18 = a3;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9440606)))) & (4)) == 0) goto loc_00604C59;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 8533719)))) & (4)) != 0) {
    }
    v_stack_p18 = (unsigned int)((unsigned int)(*(unsigned int *)(a2)));
    *(unsigned int *)(a1 + 68) = (unsigned int)((unsigned int)(v_stack_p18));
    return (unsigned int)(v_stack_p18);
}
```

## 5. (Beta) C Style

```c
int64_t RtlpHpLfhContextUpdateConfig(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    uint32_t v_stack_p18;

    v_stack_p18 = Arg3;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x900D5E)))) & (4)) == 0) goto loc_00604C59;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x8236D7)))) & (4)) != 0) {
    }
    v_stack_p18 = (uint32_t)((uint32_t)(*(uint32_t *)(arg2)));
    *(uint32_t *)(arg1 + 0x44) = (uint32_t)((uint32_t)(v_stack_p18));
    return (uint32_t)(v_stack_p18);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x44` | `32` | `W` |
| `Arg1` | `+ 0x48` | `32` | `R/W` |
| `Arg2` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00604C3C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00604C3C[BB_00604C3C]
  bb_00604C4B[BB_00604C4B]
  bb_00604C55[BB_00604C55]
  bb_00604C59[BB_00604C59]
  bb_00604C71[BB_00604C71]
  bb_00604C3C -->|branch| bb_00604C59
  bb_00604C3C -->|fallthrough| bb_00604C4B
  bb_00604C4B -->|branch| bb_00604C59
  bb_00604C4B -->|fallthrough| bb_00604C55
  bb_00604C55 -->|flow| bb_00604C59
```
