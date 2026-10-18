# SymCryptSha256Init

- RVA: `0x0051E2C0`–`0x0051E2E0` (길이 `32` bytes)
- VA: `0x000000014051E2C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SymCryptSha256](SymCryptSha256_function_0051CA8C.md) at `0x0051CACD`
- [SymCryptParallelSha256Init](SymCryptParallelSha256Init_function_0051EF2C.md) at `0x0051EF44`
- [SymCryptParallelSha256ResultDone](SymCryptParallelSha256ResultDone_function_0051F1E0.md) at `0x0051F222`
- [SepAppIdentityFromImageHash](../60/SepAppIdentityFromImageHash_function_00607AA4.md) at `0x00607C46`
- [SepAppIdentityFromPackageInformation](../60/SepAppIdentityFromPackageInformation_function_00607D7C.md) at `0x00607E68`
- [SepAppIdentityFromPackageInformation](../60/SepAppIdentityFromPackageInformation_function_00607D7C.md) at `0x00607EBD`
- [HashpInitHash](../../page/84/HashpInitHash_function_00842018.md) at `0x00842077`

### Static image references
- `0x0051E2C8` → RVA `0x0001F8B0` (`.rdata`; read)
- `0x0051E2D3` → RVA `0x0001F8C0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0051E2C0  48 83 61 10 00                  and qword ptr [rcx + 0x10], 0
0051E2C5  83 21 00                        and dword ptr [rcx], 0
0051E2C8  0F 10 05 E1 15 B0 FF            movups xmm0, xmmword ptr [rip - 0x4fea1f]
0051E2CF  0F 11 41 60                     movups xmmword ptr [rcx + 0x60], xmm0
0051E2D3  0F 10 0D E6 15 B0 FF            movups xmm1, xmmword ptr [rip - 0x4fea1a]
0051E2DA  0F 11 49 70                     movups xmmword ptr [rcx + 0x70], xmm1
0051E2DE  C3                              ret
0051E2DF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall SymCryptSha256Init(__int64 a1)
{
    *(unsigned __int64 *)(a1 + 96) = v_xmm0;
    *(unsigned __int64 *)(a1 + 112) = v_xmm1;
    return;
}
```

## 5. (Beta) C Style

```c
void SymCryptSha256Init(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    *(uint64_t *)(arg1 + 0x60) = v_xmm0;
    *(uint64_t *)(arg1 + 0x70) = v_xmm1;
    return;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R/W` |
| `Arg1` | `+ 0x10` | `64` | `R/W` |
| `Arg1` | `+ 0x60` | `128` | `R` |
| `Arg1` | `+ 0x70` | `128` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0051E2C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0051E2C0[BB_0051E2C0]
  bb_0051E2DF[BB_0051E2DF]
```
