# KiIsrThunkShadow

- RVA: `0x00BCC2C0`–`0x00BCCAC1` (길이 `2,049` bytes)
- VA: `0x0000000140BCC2C0`
- 실행 섹션: `KVASCODE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C19C0`
- 디코드: `769`개 명령, `2,049/2,049` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **256**
  - `0x00BCC2C2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC2CA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC2D2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC2DA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC2E2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC2EA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC2F2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC2FA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC302` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC30A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC312` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC31A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC322` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC32A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC332` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC33A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC342` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC34A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC352` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC35A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC362` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC36A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC372` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC37A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC382` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC38A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC392` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC39A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC3A2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC3AA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC3B2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC3BA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC3C2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC3CA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC3D2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC3DA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC3E2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC3EA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC3F2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC3FA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC402` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC40A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC412` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC41A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC422` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC42A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC432` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC43A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC442` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC44A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC452` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC45A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC462` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC46A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC472` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC47A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC482` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC48A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC492` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC49A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC4A2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC4AA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC4B2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC4BA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC4C2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC4CA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC4D2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC4DA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC4E2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC4EA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC4F2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC4FA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC502` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC50A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC512` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC51A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC522` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC52A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC532` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC53A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC542` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC54A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC552` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC55A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC562` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC56A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC572` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC57A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC582` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC58A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC592` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC59A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC5A2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC5AA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC5B2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC5BA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC5C2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC5CA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC5D2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC5DA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC5E2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC5EA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC5F2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC5FA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC602` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC60A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC612` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC61A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC622` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC62A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC632` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC63A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC642` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC64A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC652` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC65A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC662` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC66A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC672` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC67A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC682` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC68A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC692` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC69A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC6A2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC6AA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC6B2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC6BA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC6C2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC6CA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC6D2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC6DA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC6E2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC6EA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC6F2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC6FA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC702` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC70A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC712` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC71A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC722` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC72A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC732` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC73A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC742` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC74A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC752` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC75A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC762` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC76A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC772` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC77A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC782` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC78A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC792` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC79A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC7A2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC7AA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC7B2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC7BA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC7C2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC7CA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC7D2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC7DA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC7E2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC7EA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC7F2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC7FA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC802` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC80A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC812` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC81A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC822` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC82A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC832` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC83A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC842` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC84A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC852` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC85A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC862` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC86A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC872` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC87A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC882` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC88A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC892` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC89A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC8A2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC8AA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC8B2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC8BA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC8C2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC8CA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC8D2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC8DA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC8E2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC8EA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC8F2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC8FA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC902` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC90A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC912` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC91A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC922` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC92A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC932` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC93A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC942` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC94A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC952` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC95A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC962` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC96A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC972` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC97A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC982` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC98A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC992` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC99A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC9A2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC9AA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC9B2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC9BA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC9C2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC9CA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC9D2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC9DA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC9E2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC9EA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC9F2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCC9FA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCA02` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCA0A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCA12` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCA1A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCA22` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCA2A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCA32` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCA3A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCA42` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCA4A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCA52` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCA5A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCA62` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCA6A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCA72` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCA7A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCA82` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCA8A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCA92` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCA9A` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCAA2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCAAA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCAB2` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)
  - `0x00BCCABA` → [KxIsrLinkageShadow](KxIsrLinkageShadow_function_00BCCB00.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00BCC2C0  6A 00                           push 0
00BCC2C2  E9 39 08 00 00                  jmp 0x140bccb00
00BCC2C7  CC                              int3
00BCC2C8  6A 01                           push 1
00BCC2CA  E9 31 08 00 00                  jmp 0x140bccb00
00BCC2CF  CC                              int3
00BCC2D0  6A 02                           push 2
00BCC2D2  E9 29 08 00 00                  jmp 0x140bccb00
00BCC2D7  CC                              int3
00BCC2D8  6A 03                           push 3
00BCC2DA  E9 21 08 00 00                  jmp 0x140bccb00
00BCC2DF  CC                              int3
00BCC2E0  6A 04                           push 4
00BCC2E2  E9 19 08 00 00                  jmp 0x140bccb00
00BCC2E7  CC                              int3
00BCC2E8  6A 05                           push 5
00BCC2EA  E9 11 08 00 00                  jmp 0x140bccb00
00BCC2EF  CC                              int3
00BCC2F0  6A 06                           push 6
00BCC2F2  E9 09 08 00 00                  jmp 0x140bccb00
00BCC2F7  CC                              int3
00BCC2F8  6A 07                           push 7
00BCC2FA  E9 01 08 00 00                  jmp 0x140bccb00
00BCC2FF  CC                              int3
00BCC300  6A 08                           push 8
00BCC302  E9 F9 07 00 00                  jmp 0x140bccb00
00BCC307  CC                              int3
00BCC308  6A 09                           push 9
00BCC30A  E9 F1 07 00 00                  jmp 0x140bccb00
00BCC30F  CC                              int3
00BCC310  6A 0A                           push 0xa
00BCC312  E9 E9 07 00 00                  jmp 0x140bccb00
00BCC317  CC                              int3
00BCC318  6A 0B                           push 0xb
00BCC31A  E9 E1 07 00 00                  jmp 0x140bccb00
00BCC31F  CC                              int3
00BCC320  6A 0C                           push 0xc
00BCC322  E9 D9 07 00 00                  jmp 0x140bccb00
00BCC327  CC                              int3
00BCC328  6A 0D                           push 0xd
00BCC32A  E9 D1 07 00 00                  jmp 0x140bccb00
00BCC32F  CC                              int3
00BCC330  6A 0E                           push 0xe
00BCC332  E9 C9 07 00 00                  jmp 0x140bccb00
00BCC337  CC                              int3
00BCC338  6A 0F                           push 0xf
00BCC33A  E9 C1 07 00 00                  jmp 0x140bccb00
00BCC33F  CC                              int3
00BCC340  6A 10                           push 0x10
00BCC342  E9 B9 07 00 00                  jmp 0x140bccb00
00BCC347  CC                              int3
00BCC348  6A 11                           push 0x11
00BCC34A  E9 B1 07 00 00                  jmp 0x140bccb00
00BCC34F  CC                              int3
00BCC350  6A 12                           push 0x12
00BCC352  E9 A9 07 00 00                  jmp 0x140bccb00
00BCC357  CC                              int3
00BCC358  6A 13                           push 0x13
00BCC35A  E9 A1 07 00 00                  jmp 0x140bccb00
00BCC35F  CC                              int3
00BCC360  6A 14                           push 0x14
00BCC362  E9 99 07 00 00                  jmp 0x140bccb00
00BCC367  CC                              int3
00BCC368  6A 15                           push 0x15
00BCC36A  E9 91 07 00 00                  jmp 0x140bccb00
00BCC36F  CC                              int3
00BCC370  6A 16                           push 0x16
00BCC372  E9 89 07 00 00                  jmp 0x140bccb00
00BCC377  CC                              int3
00BCC378  6A 17                           push 0x17
00BCC37A  E9 81 07 00 00                  jmp 0x140bccb00
00BCC37F  CC                              int3
00BCC380  6A 18                           push 0x18
00BCC382  E9 79 07 00 00                  jmp 0x140bccb00
00BCC387  CC                              int3
00BCC388  6A 19                           push 0x19
00BCC38A  E9 71 07 00 00                  jmp 0x140bccb00
00BCC38F  CC                              int3
00BCC390  6A 1A                           push 0x1a
00BCC392  E9 69 07 00 00                  jmp 0x140bccb00
00BCC397  CC                              int3
00BCC398  6A 1B                           push 0x1b
00BCC39A  E9 61 07 00 00                  jmp 0x140bccb00
00BCC39F  CC                              int3
00BCC3A0  6A 1C                           push 0x1c
00BCC3A2  E9 59 07 00 00                  jmp 0x140bccb00
00BCC3A7  CC                              int3
00BCC3A8  6A 1D                           push 0x1d
00BCC3AA  E9 51 07 00 00                  jmp 0x140bccb00
00BCC3AF  CC                              int3
00BCC3B0  6A 1E                           push 0x1e
00BCC3B2  E9 49 07 00 00                  jmp 0x140bccb00
00BCC3B7  CC                              int3
00BCC3B8  6A 1F                           push 0x1f
00BCC3BA  E9 41 07 00 00                  jmp 0x140bccb00
00BCC3BF  CC                              int3
00BCC3C0  6A 20                           push 0x20
00BCC3C2  E9 39 07 00 00                  jmp 0x140bccb00
00BCC3C7  CC                              int3
00BCC3C8  6A 21                           push 0x21
00BCC3CA  E9 31 07 00 00                  jmp 0x140bccb00
00BCC3CF  CC                              int3
00BCC3D0  6A 22                           push 0x22
00BCC3D2  E9 29 07 00 00                  jmp 0x140bccb00
00BCC3D7  CC                              int3
00BCC3D8  6A 23                           push 0x23
00BCC3DA  E9 21 07 00 00                  jmp 0x140bccb00
00BCC3DF  CC                              int3
00BCC3E0  6A 24                           push 0x24
00BCC3E2  E9 19 07 00 00                  jmp 0x140bccb00
00BCC3E7  CC                              int3
00BCC3E8  6A 25                           push 0x25
00BCC3EA  E9 11 07 00 00                  jmp 0x140bccb00
00BCC3EF  CC                              int3
00BCC3F0  6A 26                           push 0x26
00BCC3F2  E9 09 07 00 00                  jmp 0x140bccb00
00BCC3F7  CC                              int3
00BCC3F8  6A 27                           push 0x27
00BCC3FA  E9 01 07 00 00                  jmp 0x140bccb00
00BCC3FF  CC                              int3
00BCC400  6A 28                           push 0x28
00BCC402  E9 F9 06 00 00                  jmp 0x140bccb00
00BCC407  CC                              int3
00BCC408  6A 29                           push 0x29
00BCC40A  E9 F1 06 00 00                  jmp 0x140bccb00
00BCC40F  CC                              int3
00BCC410  6A 2A                           push 0x2a
00BCC412  E9 E9 06 00 00                  jmp 0x140bccb00
00BCC417  CC                              int3
00BCC418  6A 2B                           push 0x2b
00BCC41A  E9 E1 06 00 00                  jmp 0x140bccb00
00BCC41F  CC                              int3
00BCC420  6A 2C                           push 0x2c
00BCC422  E9 D9 06 00 00                  jmp 0x140bccb00
00BCC427  CC                              int3
00BCC428  6A 2D                           push 0x2d
00BCC42A  E9 D1 06 00 00                  jmp 0x140bccb00
00BCC42F  CC                              int3
00BCC430  6A 2E                           push 0x2e
00BCC432  E9 C9 06 00 00                  jmp 0x140bccb00
00BCC437  CC                              int3
00BCC438  6A 2F                           push 0x2f
00BCC43A  E9 C1 06 00 00                  jmp 0x140bccb00
00BCC43F  CC                              int3
00BCC440  6A 30                           push 0x30
00BCC442  E9 B9 06 00 00                  jmp 0x140bccb00
00BCC447  CC                              int3
00BCC448  6A 31                           push 0x31
00BCC44A  E9 B1 06 00 00                  jmp 0x140bccb00
00BCC44F  CC                              int3
00BCC450  6A 32                           push 0x32
00BCC452  E9 A9 06 00 00                  jmp 0x140bccb00
00BCC457  CC                              int3
00BCC458  6A 33                           push 0x33
00BCC45A  E9 A1 06 00 00                  jmp 0x140bccb00
00BCC45F  CC                              int3
00BCC460  6A 34                           push 0x34
00BCC462  E9 99 06 00 00                  jmp 0x140bccb00
00BCC467  CC                              int3
00BCC468  6A 35                           push 0x35
00BCC46A  E9 91 06 00 00                  jmp 0x140bccb00
00BCC46F  CC                              int3
00BCC470  6A 36                           push 0x36
00BCC472  E9 89 06 00 00                  jmp 0x140bccb00
00BCC477  CC                              int3
00BCC478  6A 37                           push 0x37
00BCC47A  E9 81 06 00 00                  jmp 0x140bccb00
00BCC47F  CC                              int3
00BCC480  6A 38                           push 0x38
00BCC482  E9 79 06 00 00                  jmp 0x140bccb00
00BCC487  CC                              int3
00BCC488  6A 39                           push 0x39
00BCC48A  E9 71 06 00 00                  jmp 0x140bccb00
00BCC48F  CC                              int3
00BCC490  6A 3A                           push 0x3a
00BCC492  E9 69 06 00 00                  jmp 0x140bccb00
00BCC497  CC                              int3
00BCC498  6A 3B                           push 0x3b
00BCC49A  E9 61 06 00 00                  jmp 0x140bccb00
00BCC49F  CC                              int3
00BCC4A0  6A 3C                           push 0x3c
00BCC4A2  E9 59 06 00 00                  jmp 0x140bccb00
00BCC4A7  CC                              int3
00BCC4A8  6A 3D                           push 0x3d
00BCC4AA  E9 51 06 00 00                  jmp 0x140bccb00
00BCC4AF  CC                              int3
00BCC4B0  6A 3E                           push 0x3e
00BCC4B2  E9 49 06 00 00                  jmp 0x140bccb00
00BCC4B7  CC                              int3
00BCC4B8  6A 3F                           push 0x3f
00BCC4BA  E9 41 06 00 00                  jmp 0x140bccb00
00BCC4BF  CC                              int3
00BCC4C0  6A 40                           push 0x40
00BCC4C2  E9 39 06 00 00                  jmp 0x140bccb00
00BCC4C7  CC                              int3
00BCC4C8  6A 41                           push 0x41
00BCC4CA  E9 31 06 00 00                  jmp 0x140bccb00
00BCC4CF  CC                              int3
00BCC4D0  6A 42                           push 0x42
00BCC4D2  E9 29 06 00 00                  jmp 0x140bccb00
00BCC4D7  CC                              int3
00BCC4D8  6A 43                           push 0x43
00BCC4DA  E9 21 06 00 00                  jmp 0x140bccb00
00BCC4DF  CC                              int3
00BCC4E0  6A 44                           push 0x44
00BCC4E2  E9 19 06 00 00                  jmp 0x140bccb00
00BCC4E7  CC                              int3
00BCC4E8  6A 45                           push 0x45
00BCC4EA  E9 11 06 00 00                  jmp 0x140bccb00
00BCC4EF  CC                              int3
00BCC4F0  6A 46                           push 0x46
00BCC4F2  E9 09 06 00 00                  jmp 0x140bccb00
00BCC4F7  CC                              int3
00BCC4F8  6A 47                           push 0x47
00BCC4FA  E9 01 06 00 00                  jmp 0x140bccb00
00BCC4FF  CC                              int3
00BCC500  6A 48                           push 0x48
00BCC502  E9 F9 05 00 00                  jmp 0x140bccb00
00BCC507  CC                              int3
00BCC508  6A 49                           push 0x49
00BCC50A  E9 F1 05 00 00                  jmp 0x140bccb00
00BCC50F  CC                              int3
00BCC510  6A 4A                           push 0x4a
00BCC512  E9 E9 05 00 00                  jmp 0x140bccb00
00BCC517  CC                              int3
00BCC518  6A 4B                           push 0x4b
00BCC51A  E9 E1 05 00 00                  jmp 0x140bccb00
00BCC51F  CC                              int3
00BCC520  6A 4C                           push 0x4c
00BCC522  E9 D9 05 00 00                  jmp 0x140bccb00
00BCC527  CC                              int3
00BCC528  6A 4D                           push 0x4d
00BCC52A  E9 D1 05 00 00                  jmp 0x140bccb00
00BCC52F  CC                              int3
00BCC530  6A 4E                           push 0x4e
00BCC532  E9 C9 05 00 00                  jmp 0x140bccb00
00BCC537  CC                              int3
00BCC538  6A 4F                           push 0x4f
00BCC53A  E9 C1 05 00 00                  jmp 0x140bccb00
00BCC53F  CC                              int3
00BCC540  6A 50                           push 0x50
00BCC542  E9 B9 05 00 00                  jmp 0x140bccb00
00BCC547  CC                              int3
00BCC548  6A 51                           push 0x51
00BCC54A  E9 B1 05 00 00                  jmp 0x140bccb00
00BCC54F  CC                              int3
00BCC550  6A 52                           push 0x52
00BCC552  E9 A9 05 00 00                  jmp 0x140bccb00
00BCC557  CC                              int3
00BCC558  6A 53                           push 0x53
00BCC55A  E9 A1 05 00 00                  jmp 0x140bccb00
00BCC55F  CC                              int3
00BCC560  6A 54                           push 0x54
00BCC562  E9 99 05 00 00                  jmp 0x140bccb00
00BCC567  CC                              int3
00BCC568  6A 55                           push 0x55
00BCC56A  E9 91 05 00 00                  jmp 0x140bccb00
00BCC56F  CC                              int3
00BCC570  6A 56                           push 0x56
00BCC572  E9 89 05 00 00                  jmp 0x140bccb00
00BCC577  CC                              int3
00BCC578  6A 57                           push 0x57
00BCC57A  E9 81 05 00 00                  jmp 0x140bccb00
00BCC57F  CC                              int3
00BCC580  6A 58                           push 0x58
00BCC582  E9 79 05 00 00                  jmp 0x140bccb00
00BCC587  CC                              int3
00BCC588  6A 59                           push 0x59
00BCC58A  E9 71 05 00 00                  jmp 0x140bccb00
00BCC58F  CC                              int3
00BCC590  6A 5A                           push 0x5a
00BCC592  E9 69 05 00 00                  jmp 0x140bccb00
00BCC597  CC                              int3
00BCC598  6A 5B                           push 0x5b
00BCC59A  E9 61 05 00 00                  jmp 0x140bccb00
00BCC59F  CC                              int3
00BCC5A0  6A 5C                           push 0x5c
00BCC5A2  E9 59 05 00 00                  jmp 0x140bccb00
00BCC5A7  CC                              int3
00BCC5A8  6A 5D                           push 0x5d
00BCC5AA  E9 51 05 00 00                  jmp 0x140bccb00
00BCC5AF  CC                              int3
00BCC5B0  6A 5E                           push 0x5e
00BCC5B2  E9 49 05 00 00                  jmp 0x140bccb00
00BCC5B7  CC                              int3
00BCC5B8  6A 5F                           push 0x5f
00BCC5BA  E9 41 05 00 00                  jmp 0x140bccb00
00BCC5BF  CC                              int3
00BCC5C0  6A 60                           push 0x60
00BCC5C2  E9 39 05 00 00                  jmp 0x140bccb00
00BCC5C7  CC                              int3
00BCC5C8  6A 61                           push 0x61
00BCC5CA  E9 31 05 00 00                  jmp 0x140bccb00
00BCC5CF  CC                              int3
00BCC5D0  6A 62                           push 0x62
00BCC5D2  E9 29 05 00 00                  jmp 0x140bccb00
00BCC5D7  CC                              int3
00BCC5D8  6A 63                           push 0x63
00BCC5DA  E9 21 05 00 00                  jmp 0x140bccb00
00BCC5DF  CC                              int3
00BCC5E0  6A 64                           push 0x64
00BCC5E2  E9 19 05 00 00                  jmp 0x140bccb00
00BCC5E7  CC                              int3
00BCC5E8  6A 65                           push 0x65
00BCC5EA  E9 11 05 00 00                  jmp 0x140bccb00
00BCC5EF  CC                              int3
00BCC5F0  6A 66                           push 0x66
00BCC5F2  E9 09 05 00 00                  jmp 0x140bccb00
00BCC5F7  CC                              int3
00BCC5F8  6A 67                           push 0x67
00BCC5FA  E9 01 05 00 00                  jmp 0x140bccb00
00BCC5FF  CC                              int3
00BCC600  6A 68                           push 0x68
00BCC602  E9 F9 04 00 00                  jmp 0x140bccb00
00BCC607  CC                              int3
00BCC608  6A 69                           push 0x69
00BCC60A  E9 F1 04 00 00                  jmp 0x140bccb00
00BCC60F  CC                              int3
00BCC610  6A 6A                           push 0x6a
00BCC612  E9 E9 04 00 00                  jmp 0x140bccb00
00BCC617  CC                              int3
00BCC618  6A 6B                           push 0x6b
00BCC61A  E9 E1 04 00 00                  jmp 0x140bccb00
00BCC61F  CC                              int3
00BCC620  6A 6C                           push 0x6c
00BCC622  E9 D9 04 00 00                  jmp 0x140bccb00
00BCC627  CC                              int3
00BCC628  6A 6D                           push 0x6d
00BCC62A  E9 D1 04 00 00                  jmp 0x140bccb00
00BCC62F  CC                              int3
00BCC630  6A 6E                           push 0x6e
00BCC632  E9 C9 04 00 00                  jmp 0x140bccb00
00BCC637  CC                              int3
00BCC638  6A 6F                           push 0x6f
00BCC63A  E9 C1 04 00 00                  jmp 0x140bccb00
00BCC63F  CC                              int3
00BCC640  6A 70                           push 0x70
00BCC642  E9 B9 04 00 00                  jmp 0x140bccb00
00BCC647  CC                              int3
00BCC648  6A 71                           push 0x71
00BCC64A  E9 B1 04 00 00                  jmp 0x140bccb00
00BCC64F  CC                              int3
00BCC650  6A 72                           push 0x72
00BCC652  E9 A9 04 00 00                  jmp 0x140bccb00
00BCC657  CC                              int3
00BCC658  6A 73                           push 0x73
00BCC65A  E9 A1 04 00 00                  jmp 0x140bccb00
00BCC65F  CC                              int3
00BCC660  6A 74                           push 0x74
00BCC662  E9 99 04 00 00                  jmp 0x140bccb00
00BCC667  CC                              int3
00BCC668  6A 75                           push 0x75
00BCC66A  E9 91 04 00 00                  jmp 0x140bccb00
00BCC66F  CC                              int3
00BCC670  6A 76                           push 0x76
00BCC672  E9 89 04 00 00                  jmp 0x140bccb00
00BCC677  CC                              int3
00BCC678  6A 77                           push 0x77
00BCC67A  E9 81 04 00 00                  jmp 0x140bccb00
00BCC67F  CC                              int3
00BCC680  6A 78                           push 0x78
00BCC682  E9 79 04 00 00                  jmp 0x140bccb00
00BCC687  CC                              int3
00BCC688  6A 79                           push 0x79
00BCC68A  E9 71 04 00 00                  jmp 0x140bccb00
00BCC68F  CC                              int3
00BCC690  6A 7A                           push 0x7a
00BCC692  E9 69 04 00 00                  jmp 0x140bccb00
00BCC697  CC                              int3
00BCC698  6A 7B                           push 0x7b
00BCC69A  E9 61 04 00 00                  jmp 0x140bccb00
00BCC69F  CC                              int3
00BCC6A0  6A 7C                           push 0x7c
00BCC6A2  E9 59 04 00 00                  jmp 0x140bccb00
00BCC6A7  CC                              int3
00BCC6A8  6A 7D                           push 0x7d
00BCC6AA  E9 51 04 00 00                  jmp 0x140bccb00
00BCC6AF  CC                              int3
00BCC6B0  6A 7E                           push 0x7e
00BCC6B2  E9 49 04 00 00                  jmp 0x140bccb00
00BCC6B7  CC                              int3
00BCC6B8  6A 7F                           push 0x7f
00BCC6BA  E9 41 04 00 00                  jmp 0x140bccb00
00BCC6BF  CC                              int3
00BCC6C0  6A 80                           push -0x80
00BCC6C2  E9 39 04 00 00                  jmp 0x140bccb00
00BCC6C7  CC                              int3
00BCC6C8  6A 81                           push -0x7f
00BCC6CA  E9 31 04 00 00                  jmp 0x140bccb00
00BCC6CF  CC                              int3
00BCC6D0  6A 82                           push -0x7e
00BCC6D2  E9 29 04 00 00                  jmp 0x140bccb00
00BCC6D7  CC                              int3
00BCC6D8  6A 83                           push -0x7d
00BCC6DA  E9 21 04 00 00                  jmp 0x140bccb00
00BCC6DF  CC                              int3
00BCC6E0  6A 84                           push -0x7c
00BCC6E2  E9 19 04 00 00                  jmp 0x140bccb00
00BCC6E7  CC                              int3
00BCC6E8  6A 85                           push -0x7b
00BCC6EA  E9 11 04 00 00                  jmp 0x140bccb00
00BCC6EF  CC                              int3
00BCC6F0  6A 86                           push -0x7a
00BCC6F2  E9 09 04 00 00                  jmp 0x140bccb00
00BCC6F7  CC                              int3
00BCC6F8  6A 87                           push -0x79
00BCC6FA  E9 01 04 00 00                  jmp 0x140bccb00
00BCC6FF  CC                              int3
00BCC700  6A 88                           push -0x78
00BCC702  E9 F9 03 00 00                  jmp 0x140bccb00
00BCC707  CC                              int3
00BCC708  6A 89                           push -0x77
00BCC70A  E9 F1 03 00 00                  jmp 0x140bccb00
00BCC70F  CC                              int3
00BCC710  6A 8A                           push -0x76
00BCC712  E9 E9 03 00 00                  jmp 0x140bccb00
00BCC717  CC                              int3
00BCC718  6A 8B                           push -0x75
00BCC71A  E9 E1 03 00 00                  jmp 0x140bccb00
00BCC71F  CC                              int3
00BCC720  6A 8C                           push -0x74
00BCC722  E9 D9 03 00 00                  jmp 0x140bccb00
00BCC727  CC                              int3
00BCC728  6A 8D                           push -0x73
00BCC72A  E9 D1 03 00 00                  jmp 0x140bccb00
00BCC72F  CC                              int3
00BCC730  6A 8E                           push -0x72
00BCC732  E9 C9 03 00 00                  jmp 0x140bccb00
00BCC737  CC                              int3
00BCC738  6A 8F                           push -0x71
00BCC73A  E9 C1 03 00 00                  jmp 0x140bccb00
00BCC73F  CC                              int3
00BCC740  6A 90                           push -0x70
00BCC742  E9 B9 03 00 00                  jmp 0x140bccb00
00BCC747  CC                              int3
00BCC748  6A 91                           push -0x6f
00BCC74A  E9 B1 03 00 00                  jmp 0x140bccb00
00BCC74F  CC                              int3
00BCC750  6A 92                           push -0x6e
00BCC752  E9 A9 03 00 00                  jmp 0x140bccb00
00BCC757  CC                              int3
00BCC758  6A 93                           push -0x6d
00BCC75A  E9 A1 03 00 00                  jmp 0x140bccb00
00BCC75F  CC                              int3
00BCC760  6A 94                           push -0x6c
00BCC762  E9 99 03 00 00                  jmp 0x140bccb00
00BCC767  CC                              int3
00BCC768  6A 95                           push -0x6b
00BCC76A  E9 91 03 00 00                  jmp 0x140bccb00
00BCC76F  CC                              int3
00BCC770  6A 96                           push -0x6a
00BCC772  E9 89 03 00 00                  jmp 0x140bccb00
00BCC777  CC                              int3
00BCC778  6A 97                           push -0x69
00BCC77A  E9 81 03 00 00                  jmp 0x140bccb00
00BCC77F  CC                              int3
00BCC780  6A 98                           push -0x68
00BCC782  E9 79 03 00 00                  jmp 0x140bccb00
00BCC787  CC                              int3
00BCC788  6A 99                           push -0x67
00BCC78A  E9 71 03 00 00                  jmp 0x140bccb00
00BCC78F  CC                              int3
00BCC790  6A 9A                           push -0x66
00BCC792  E9 69 03 00 00                  jmp 0x140bccb00
00BCC797  CC                              int3
00BCC798  6A 9B                           push -0x65
00BCC79A  E9 61 03 00 00                  jmp 0x140bccb00
00BCC79F  CC                              int3
00BCC7A0  6A 9C                           push -0x64
00BCC7A2  E9 59 03 00 00                  jmp 0x140bccb00
00BCC7A7  CC                              int3
00BCC7A8  6A 9D                           push -0x63
00BCC7AA  E9 51 03 00 00                  jmp 0x140bccb00
00BCC7AF  CC                              int3
00BCC7B0  6A 9E                           push -0x62
00BCC7B2  E9 49 03 00 00                  jmp 0x140bccb00
00BCC7B7  CC                              int3
00BCC7B8  6A 9F                           push -0x61
00BCC7BA  E9 41 03 00 00                  jmp 0x140bccb00
00BCC7BF  CC                              int3
00BCC7C0  6A A0                           push -0x60
00BCC7C2  E9 39 03 00 00                  jmp 0x140bccb00
00BCC7C7  CC                              int3
00BCC7C8  6A A1                           push -0x5f
00BCC7CA  E9 31 03 00 00                  jmp 0x140bccb00
00BCC7CF  CC                              int3
00BCC7D0  6A A2                           push -0x5e
00BCC7D2  E9 29 03 00 00                  jmp 0x140bccb00
00BCC7D7  CC                              int3
00BCC7D8  6A A3                           push -0x5d
00BCC7DA  E9 21 03 00 00                  jmp 0x140bccb00
00BCC7DF  CC                              int3
00BCC7E0  6A A4                           push -0x5c
00BCC7E2  E9 19 03 00 00                  jmp 0x140bccb00
00BCC7E7  CC                              int3
00BCC7E8  6A A5                           push -0x5b
00BCC7EA  E9 11 03 00 00                  jmp 0x140bccb00
00BCC7EF  CC                              int3
00BCC7F0  6A A6                           push -0x5a
00BCC7F2  E9 09 03 00 00                  jmp 0x140bccb00
00BCC7F7  CC                              int3
00BCC7F8  6A A7                           push -0x59
00BCC7FA  E9 01 03 00 00                  jmp 0x140bccb00
00BCC7FF  CC                              int3
00BCC800  6A A8                           push -0x58
00BCC802  E9 F9 02 00 00                  jmp 0x140bccb00
00BCC807  CC                              int3
00BCC808  6A A9                           push -0x57
00BCC80A  E9 F1 02 00 00                  jmp 0x140bccb00
00BCC80F  CC                              int3
00BCC810  6A AA                           push -0x56
00BCC812  E9 E9 02 00 00                  jmp 0x140bccb00
00BCC817  CC                              int3
00BCC818  6A AB                           push -0x55
00BCC81A  E9 E1 02 00 00                  jmp 0x140bccb00
00BCC81F  CC                              int3
00BCC820  6A AC                           push -0x54
00BCC822  E9 D9 02 00 00                  jmp 0x140bccb00
00BCC827  CC                              int3
00BCC828  6A AD                           push -0x53
00BCC82A  E9 D1 02 00 00                  jmp 0x140bccb00
00BCC82F  CC                              int3
00BCC830  6A AE                           push -0x52
00BCC832  E9 C9 02 00 00                  jmp 0x140bccb00
00BCC837  CC                              int3
00BCC838  6A AF                           push -0x51
00BCC83A  E9 C1 02 00 00                  jmp 0x140bccb00
00BCC83F  CC                              int3
00BCC840  6A B0                           push -0x50
00BCC842  E9 B9 02 00 00                  jmp 0x140bccb00
00BCC847  CC                              int3
00BCC848  6A B1                           push -0x4f
00BCC84A  E9 B1 02 00 00                  jmp 0x140bccb00
00BCC84F  CC                              int3
00BCC850  6A B2                           push -0x4e
00BCC852  E9 A9 02 00 00                  jmp 0x140bccb00
00BCC857  CC                              int3
00BCC858  6A B3                           push -0x4d
00BCC85A  E9 A1 02 00 00                  jmp 0x140bccb00
00BCC85F  CC                              int3
00BCC860  6A B4                           push -0x4c
00BCC862  E9 99 02 00 00                  jmp 0x140bccb00
00BCC867  CC                              int3
00BCC868  6A B5                           push -0x4b
00BCC86A  E9 91 02 00 00                  jmp 0x140bccb00
00BCC86F  CC                              int3
00BCC870  6A B6                           push -0x4a
00BCC872  E9 89 02 00 00                  jmp 0x140bccb00
00BCC877  CC                              int3
00BCC878  6A B7                           push -0x49
00BCC87A  E9 81 02 00 00                  jmp 0x140bccb00
00BCC87F  CC                              int3
00BCC880  6A B8                           push -0x48
00BCC882  E9 79 02 00 00                  jmp 0x140bccb00
00BCC887  CC                              int3
00BCC888  6A B9                           push -0x47
00BCC88A  E9 71 02 00 00                  jmp 0x140bccb00
00BCC88F  CC                              int3
00BCC890  6A BA                           push -0x46
00BCC892  E9 69 02 00 00                  jmp 0x140bccb00
00BCC897  CC                              int3
00BCC898  6A BB                           push -0x45
00BCC89A  E9 61 02 00 00                  jmp 0x140bccb00
00BCC89F  CC                              int3
00BCC8A0  6A BC                           push -0x44
00BCC8A2  E9 59 02 00 00                  jmp 0x140bccb00
00BCC8A7  CC                              int3
00BCC8A8  6A BD                           push -0x43
00BCC8AA  E9 51 02 00 00                  jmp 0x140bccb00
00BCC8AF  CC                              int3
00BCC8B0  6A BE                           push -0x42
00BCC8B2  E9 49 02 00 00                  jmp 0x140bccb00
00BCC8B7  CC                              int3
00BCC8B8  6A BF                           push -0x41
00BCC8BA  E9 41 02 00 00                  jmp 0x140bccb00
00BCC8BF  CC                              int3
00BCC8C0  6A C0                           push -0x40
00BCC8C2  E9 39 02 00 00                  jmp 0x140bccb00
00BCC8C7  CC                              int3
00BCC8C8  6A C1                           push -0x3f
00BCC8CA  E9 31 02 00 00                  jmp 0x140bccb00
00BCC8CF  CC                              int3
00BCC8D0  6A C2                           push -0x3e
00BCC8D2  E9 29 02 00 00                  jmp 0x140bccb00
00BCC8D7  CC                              int3
00BCC8D8  6A C3                           push -0x3d
00BCC8DA  E9 21 02 00 00                  jmp 0x140bccb00
00BCC8DF  CC                              int3
00BCC8E0  6A C4                           push -0x3c
00BCC8E2  E9 19 02 00 00                  jmp 0x140bccb00
00BCC8E7  CC                              int3
00BCC8E8  6A C5                           push -0x3b
00BCC8EA  E9 11 02 00 00                  jmp 0x140bccb00
00BCC8EF  CC                              int3
00BCC8F0  6A C6                           push -0x3a
00BCC8F2  E9 09 02 00 00                  jmp 0x140bccb00
00BCC8F7  CC                              int3
00BCC8F8  6A C7                           push -0x39
00BCC8FA  E9 01 02 00 00                  jmp 0x140bccb00
00BCC8FF  CC                              int3
00BCC900  6A C8                           push -0x38
00BCC902  E9 F9 01 00 00                  jmp 0x140bccb00
00BCC907  CC                              int3
00BCC908  6A C9                           push -0x37
00BCC90A  E9 F1 01 00 00                  jmp 0x140bccb00
00BCC90F  CC                              int3
00BCC910  6A CA                           push -0x36
00BCC912  E9 E9 01 00 00                  jmp 0x140bccb00
00BCC917  CC                              int3
00BCC918  6A CB                           push -0x35
00BCC91A  E9 E1 01 00 00                  jmp 0x140bccb00
00BCC91F  CC                              int3
00BCC920  6A CC                           push -0x34
00BCC922  E9 D9 01 00 00                  jmp 0x140bccb00
00BCC927  CC                              int3
00BCC928  6A CD                           push -0x33
00BCC92A  E9 D1 01 00 00                  jmp 0x140bccb00
00BCC92F  CC                              int3
00BCC930  6A CE                           push -0x32
00BCC932  E9 C9 01 00 00                  jmp 0x140bccb00
00BCC937  CC                              int3
00BCC938  6A CF                           push -0x31
00BCC93A  E9 C1 01 00 00                  jmp 0x140bccb00
00BCC93F  CC                              int3
00BCC940  6A D0                           push -0x30
00BCC942  E9 B9 01 00 00                  jmp 0x140bccb00
00BCC947  CC                              int3
00BCC948  6A D1                           push -0x2f
00BCC94A  E9 B1 01 00 00                  jmp 0x140bccb00
00BCC94F  CC                              int3
00BCC950  6A D2                           push -0x2e
00BCC952  E9 A9 01 00 00                  jmp 0x140bccb00
00BCC957  CC                              int3
00BCC958  6A D3                           push -0x2d
00BCC95A  E9 A1 01 00 00                  jmp 0x140bccb00
00BCC95F  CC                              int3
00BCC960  6A D4                           push -0x2c
00BCC962  E9 99 01 00 00                  jmp 0x140bccb00
00BCC967  CC                              int3
00BCC968  6A D5                           push -0x2b
00BCC96A  E9 91 01 00 00                  jmp 0x140bccb00
00BCC96F  CC                              int3
00BCC970  6A D6                           push -0x2a
00BCC972  E9 89 01 00 00                  jmp 0x140bccb00
00BCC977  CC                              int3
00BCC978  6A D7                           push -0x29
00BCC97A  E9 81 01 00 00                  jmp 0x140bccb00
00BCC97F  CC                              int3
00BCC980  6A D8                           push -0x28
00BCC982  E9 79 01 00 00                  jmp 0x140bccb00
00BCC987  CC                              int3
00BCC988  6A D9                           push -0x27
00BCC98A  E9 71 01 00 00                  jmp 0x140bccb00
00BCC98F  CC                              int3
00BCC990  6A DA                           push -0x26
00BCC992  E9 69 01 00 00                  jmp 0x140bccb00
00BCC997  CC                              int3
00BCC998  6A DB                           push -0x25
00BCC99A  E9 61 01 00 00                  jmp 0x140bccb00
00BCC99F  CC                              int3
00BCC9A0  6A DC                           push -0x24
00BCC9A2  E9 59 01 00 00                  jmp 0x140bccb00
00BCC9A7  CC                              int3
00BCC9A8  6A DD                           push -0x23
00BCC9AA  E9 51 01 00 00                  jmp 0x140bccb00
00BCC9AF  CC                              int3
00BCC9B0  6A DE                           push -0x22
00BCC9B2  E9 49 01 00 00                  jmp 0x140bccb00
00BCC9B7  CC                              int3
00BCC9B8  6A DF                           push -0x21
00BCC9BA  E9 41 01 00 00                  jmp 0x140bccb00
00BCC9BF  CC                              int3
00BCC9C0  6A E0                           push -0x20
00BCC9C2  E9 39 01 00 00                  jmp 0x140bccb00
00BCC9C7  CC                              int3
00BCC9C8  6A E1                           push -0x1f
00BCC9CA  E9 31 01 00 00                  jmp 0x140bccb00
00BCC9CF  CC                              int3
00BCC9D0  6A E2                           push -0x1e
00BCC9D2  E9 29 01 00 00                  jmp 0x140bccb00
00BCC9D7  CC                              int3
00BCC9D8  6A E3                           push -0x1d
00BCC9DA  E9 21 01 00 00                  jmp 0x140bccb00
00BCC9DF  CC                              int3
00BCC9E0  6A E4                           push -0x1c
00BCC9E2  E9 19 01 00 00                  jmp 0x140bccb00
00BCC9E7  CC                              int3
00BCC9E8  6A E5                           push -0x1b
00BCC9EA  E9 11 01 00 00                  jmp 0x140bccb00
00BCC9EF  CC                              int3
00BCC9F0  6A E6                           push -0x1a
00BCC9F2  E9 09 01 00 00                  jmp 0x140bccb00
00BCC9F7  CC                              int3
00BCC9F8  6A E7                           push -0x19
00BCC9FA  E9 01 01 00 00                  jmp 0x140bccb00
00BCC9FF  CC                              int3
00BCCA00  6A E8                           push -0x18
00BCCA02  E9 F9 00 00 00                  jmp 0x140bccb00
00BCCA07  CC                              int3
00BCCA08  6A E9                           push -0x17
00BCCA0A  E9 F1 00 00 00                  jmp 0x140bccb00
00BCCA0F  CC                              int3
00BCCA10  6A EA                           push -0x16
00BCCA12  E9 E9 00 00 00                  jmp 0x140bccb00
00BCCA17  CC                              int3
00BCCA18  6A EB                           push -0x15
00BCCA1A  E9 E1 00 00 00                  jmp 0x140bccb00
00BCCA1F  CC                              int3
00BCCA20  6A EC                           push -0x14
00BCCA22  E9 D9 00 00 00                  jmp 0x140bccb00
00BCCA27  CC                              int3
00BCCA28  6A ED                           push -0x13
00BCCA2A  E9 D1 00 00 00                  jmp 0x140bccb00
00BCCA2F  CC                              int3
00BCCA30  6A EE                           push -0x12
00BCCA32  E9 C9 00 00 00                  jmp 0x140bccb00
00BCCA37  CC                              int3
00BCCA38  6A EF                           push -0x11
00BCCA3A  E9 C1 00 00 00                  jmp 0x140bccb00
00BCCA3F  CC                              int3
00BCCA40  6A F0                           push -0x10
00BCCA42  E9 B9 00 00 00                  jmp 0x140bccb00
00BCCA47  CC                              int3
00BCCA48  6A F1                           push -0xf
00BCCA4A  E9 B1 00 00 00                  jmp 0x140bccb00
00BCCA4F  CC                              int3
00BCCA50  6A F2                           push -0xe
00BCCA52  E9 A9 00 00 00                  jmp 0x140bccb00
00BCCA57  CC                              int3
00BCCA58  6A F3                           push -0xd
00BCCA5A  E9 A1 00 00 00                  jmp 0x140bccb00
00BCCA5F  CC                              int3
00BCCA60  6A F4                           push -0xc
00BCCA62  E9 99 00 00 00                  jmp 0x140bccb00
00BCCA67  CC                              int3
00BCCA68  6A F5                           push -0xb
00BCCA6A  E9 91 00 00 00                  jmp 0x140bccb00
00BCCA6F  CC                              int3
00BCCA70  6A F6                           push -0xa
00BCCA72  E9 89 00 00 00                  jmp 0x140bccb00
00BCCA77  CC                              int3
00BCCA78  6A F7                           push -9
00BCCA7A  E9 81 00 00 00                  jmp 0x140bccb00
00BCCA7F  CC                              int3
00BCCA80  6A F8                           push -8
00BCCA82  E9 79 00 00 00                  jmp 0x140bccb00
00BCCA87  CC                              int3
00BCCA88  6A F9                           push -7
00BCCA8A  E9 71 00 00 00                  jmp 0x140bccb00
00BCCA8F  CC                              int3
00BCCA90  6A FA                           push -6
00BCCA92  E9 69 00 00 00                  jmp 0x140bccb00
00BCCA97  CC                              int3
00BCCA98  6A FB                           push -5
00BCCA9A  E9 61 00 00 00                  jmp 0x140bccb00
00BCCA9F  CC                              int3
00BCCAA0  6A FC                           push -4
00BCCAA2  E9 59 00 00 00                  jmp 0x140bccb00
00BCCAA7  CC                              int3
00BCCAA8  6A FD                           push -3
00BCCAAA  E9 51 00 00 00                  jmp 0x140bccb00
00BCCAAF  CC                              int3
00BCCAB0  6A FE                           push -2
00BCCAB2  E9 49 00 00 00                  jmp 0x140bccb00
00BCCAB7  CC                              int3
00BCCAB8  6A FF                           push -1
00BCCABA  E9 41 00 00 00                  jmp 0x140bccb00
00BCCABF  CC                              int3
00BCCAC0  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall KiIsrThunkShadow(void)
{
}
```

## 5. (Beta) C Style

```c
void KiIsrThunkShadow(void)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=kvascode&rva=0x00BCC2C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
