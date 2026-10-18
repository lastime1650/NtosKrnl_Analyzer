# AdtpEtwBuildDashString

- RVA: `0x00AAB7B0`–`0x00AAB7C7` (길이 `23` bytes)
- VA: `0x0000000140AAB7B0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `23/23` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [AdtpBuildAccessReasonAuditString](../../text/40/AdtpBuildAccessReasonAuditString_function_0040EE04.md) at `0x0040EEBF`
- [AdtpPackageParameters](../../text/45/AdtpPackageParameters_function_00459964.md) at `0x00459FED`
- [AdtpPackageParameters](../../text/45/AdtpPackageParameters_function_00459964.md) at `0x0045A030`
- [AdtpBuildMultiSzStringListString](../../text/45/AdtpBuildMultiSzStringListString_function_0045A388.md) at `0x0045A4F3`
- [sub_006F1C3C](../../text/6F/Unknown_function_006F1C3C.md) at `0x006F1C47`

### Static image references
- `0x00AAB7B4` → RVA `0x0001E0B0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AAB7B0  83 61 0C 00                     and dword ptr [rcx + 0xc], 0
00AAB7B4  48 8D 05 F5 28 57 FF            lea rax, [rip - 0xa8d70b]
00AAB7BB  48 89 01                        mov qword ptr [rcx], rax
00AAB7BE  C7 41 08 04 00 00 00            mov dword ptr [rcx + 8], 4
00AAB7C5  C3                              ret
00AAB7C6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AdtpEtwBuildDashString(__int64 a1)
{
    *(unsigned __int64 *)(a1) = v_rip - 11065099;
    *(unsigned int *)(a1 + 8) = 4;
    return v_rip - 11065099;
}
```

## 5. (Beta) C Style

```c
int64_t AdtpEtwBuildDashString(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    *(uint64_t *)(arg1) = v_rip - 11065099;
    *(uint32_t *)(arg1 + 0x8) = 4;
    return v_rip - 11065099;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `32` | `W` |
| `Arg1` | `+ 0xC` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AAB7B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AAB7B0[BB_00AAB7B0]
  bb_00AAB7C6[BB_00AAB7C6]
```
