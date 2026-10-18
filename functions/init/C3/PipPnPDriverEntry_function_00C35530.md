# PipPnPDriverEntry

- RVA: `0x00C35530`–`0x00C35574` (길이 `68` bytes)
- VA: `0x0000000140C35530`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `13`개 명령, `68/68` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00C35534` → RVA `0x00A97CF0` (`ArbPreprocessEntry`; read)
- `0x00C3553B` → RVA `0x00F8C440` (`.data`; write)
- `0x00C35546` → RVA `0x00A74B90` (`IopPnPDispatch`; read)
- `0x00C35554` → RVA `0x00470BF0` (`IopPowerDispatch`; read)
- `0x00C35562` → RVA `0x00737DA0` (`IopSystemControlDispatch`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C35530  48 8B 41 30                     mov rax, qword ptr [rcx + 0x30]
00C35534  48 8D 15 B5 27 E6 FF            lea rdx, [rip - 0x19d84b]
00C3553B  48 89 0D FE 6E 35 00            mov qword ptr [rip + 0x356efe], rcx
00C35542  48 89 50 08                     mov qword ptr [rax + 8], rdx
00C35546  48 8D 05 43 F6 E3 FF            lea rax, [rip - 0x1c09bd]
00C3554D  48 89 81 48 01 00 00            mov qword ptr [rcx + 0x148], rax
00C35554  48 8D 05 95 B6 83 FF            lea rax, [rip - 0x7c496b]
00C3555B  48 89 81 20 01 00 00            mov qword ptr [rcx + 0x120], rax
00C35562  48 8D 05 37 28 B0 FF            lea rax, [rip - 0x4fd7c9]
00C35569  48 89 81 28 01 00 00            mov qword ptr [rcx + 0x128], rax
00C35570  33 C0                           xor eax, eax
00C35572  C3                              ret
00C35573  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PipPnPDriverEntry(__int64 a1)
{
    __int64 result;

    *(unsigned __int64 *)(v_rip + 3501822) = a1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 8) = v_rip - 1693771;
    *(unsigned __int64 *)(a1 + 328) = v_rip - 1837501;
    *(unsigned __int64 *)(a1 + 288) = v_rip - 8145259;
    *(unsigned __int64 *)(a1 + 296) = v_rip - 5232585;
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PipPnPDriverEntry(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    *(void **)(v_rip + 0x356EFE) = Arg1;
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x8) = v_rip - 1693771;
    *(uint64_t *)(arg1 + 0x148) = v_rip - 1837501;
    *(uint64_t *)(arg1 + 0x120) = v_rip - 8145259;
    *(uint64_t *)(arg1 + 0x128) = v_rip - 5232585;
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x120` | `64` | `W` |
| `Arg1` | `+ 0x128` | `64` | `W` |
| `Arg1` | `+ 0x148` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C35530&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C35530[BB_00C35530]
  bb_00C35573[BB_00C35573]
```
